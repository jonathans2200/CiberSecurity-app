import os
import asyncio
import logging
import ast
from contextlib import AsyncExitStack

from dotenv import load_dotenv
from mcp import ClientSession, StdioServerParameters, types
from mcp.client.stdio import stdio_client
import openai

import json
from urllib.parse import urlparse
import base64

load_dotenv()

class MCPClient:
    def __init__(self):
        # Read credentials and commands
        self.server_cmd = os.getenv("MCP_SERVER_CMD")
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self._stack = AsyncExitStack()
        self.session: ClientSession | None = None

    async def connect_to_server(self):
        print(f"Connecting to server using command: {self.server_cmd}")
        # Launch MCP server as subprocess
        server_params = StdioServerParameters(
            command=self.server_cmd.split()[0],
            args=self.server_cmd.split()[1:],
            env=None
        )
        # Establish read/write streams
        read, write = await self._stack.enter_async_context (
            stdio_client(server_params)
        )
        # Create and initialize the client session
        self.session = await self._stack.enter_async_context(
            ClientSession(read, write)
        )
        await self.session.initialize()

        # Cache available tools
        self.available_tools = await self.session.list_tools()
        print(f"Available tools: {self.available_tools}")

    async def call_tool(self, name: str, arguments: dict):
        # Get list of tool names from the Tool objects
        if not self.session:
            raise RuntimeError("No active session")
        
        tool_names = [tool.name for tool in self.available_tools.tools]
        if name not in tool_names:
            raise RuntimeError(f"Tool {name} not defined")
        return await self.session.call_tool(name, arguments=arguments)

    async def augment_report(self, raw_report: dict, value: str) -> dict:
        
        # Detect if it is URL or IP or Archive
        def detect_entity_type(raw_report: dict) -> str:
            entity_type = raw_report.get("data", {}).get("type")
            if entity_type == "file":
                return "file"
            elif entity_type == "ip_address":
                return "ip"
            elif entity_type in ("url", "analysis"):
                return "url"
            else:
                raise ValueError("El informe no pertenece a ninguna URL, IP o Archivo")
        
        # Process URL
        tipo = detect_entity_type(raw_report)
        expanded = {}
        # TEST PRINT
        print(f"TIPO: {tipo}\n")

        if tipo == "url":
            url = value
            if not url:
                raise ValueError("No se pudo extraer el URL")
            domain = urlparse(url).netloc
            # TEST PRINT
            print(f"DOMAIN: {domain}\n")
            # WHOIS lookup
            whois_info = await self.call_tool("whois_lookup", {"domain": domain})
            # TEST PRINT
            print(f"WHOIS_INFO: {whois_info}\n")
            if hasattr(whois_info, 'content') and not whois_info.isError:
                whois_data = whois_info.content[0].text
            else:
                whois_data = {"error": "Failed to get WHOIS info"}
                
            expanded = {"virus_total_report": raw_report, "whois_info": whois_data}

        # Process IP
        elif tipo == "ip":
            ip_address = value
            if not ip_address:
                raise ValueError("No se pudo extraer el IP")
            
            #AbuseIPDB lookup
            abuse_info = await self.call_tool("abuse_ipdb_lookup", {"ip": ip_address})
            expanded = {"virus_total_report": raw_report, "abuse_ipdb_info": abuse_info}
        
        # Process Archive
        else:
            expanded = {"virus_total_report": raw_report}
        
        # TEST PRINT
        print(f"EXPANDED: {expanded}\n")
        # LLM Enrichment
        client = openai.OpenAI()
        try:
            response = client.chat.completions.create(
                model="gpt-4o-mini",
                max_tokens=3000,
                messages=[
                    {"role": "system", "content": "Eres un analista de ciberseguridad"},
                    {"role": "user", "content": f"Analiza el siguiente reporte de seguridad de VirusTotal y genera un informe expandido de al menos 800 palabras, tecnico y detallado. \
                                                 Si detectas que el {tipo} tiene amenazas, sugiere medidas de seguridad para mitigar riesgos. \
                                                 Por favor, proporciona: \
                                                 - Un resumen general del estado. \
                                                 - Principales riesgos encontrados (si los hay). \
                                                 - Recomendaciones de seguridad si aplica. \
                                                 - Incluye datos especificos como fecha de creacion del dominio o IP (si aplica) y registrante o personas/entidades identificadas como responsables. \
                                                 - Reporte de Virus Total API y Whois API ó AbuseIPDB API: {expanded}"}
                ], response_format={
                    "type": "text"
                },
                temperature=0.5,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0,
                store=False
            )
        except Exception as e:
            logging.error(f"OpenAI API error: {e}")
            response = None

        if response is None:
            return {
                "report": "Error generating report from OpenAI",
                "pdf_base64": ""
            }
        
        report_text = response.choices[0].message.content

        # Generate PDF
        pdf_result = await self.call_tool("export_pdf", {"report_text": report_text})

        # --- ADD LOGGING HERE ---
        print("\n--- Debugging PDF Result ---")
        print(f"Type of pdf_result: {type(pdf_result)}")
        print(f"pdf_result object: {pdf_result}")
        if hasattr(pdf_result, 'content') and pdf_result.content:
            print(f"Type of pdf_result.content[0]: {type(pdf_result.content[0])}")
            print(f"Content object: {pdf_result.content[0]}")
            if hasattr(pdf_result.content[0], 'blob'):
                print(f"Blob content preview: {pdf_result.content[0].blob[:30]}") # Show first 30 bytes
            elif hasattr(pdf_result.content[0], 'text'):
                print(f"Text content preview: {pdf_result.content[0].text[:30] if isinstance(pdf_result.content[0].text, (str, bytes)) else type(pdf_result.content[0].text)}")
        print("---------------------------\n")
        # --- END LOGGING ---

        # Extract PDF bytes from the result
        pdf_bytes_content = b"Error generating PDF" # Default error value
        if hasattr(pdf_result, 'content') and not pdf_result.isError and pdf_result.content:
            if len(pdf_result.content) > 0:
                content_item = pdf_result.content[0]
                if hasattr(content_item, 'blob'): # Ideal case: BlobContent
                    pdf_bytes_content = content_item.blob
                    print("Extracted PDF bytes from BLOB")
                elif hasattr(content_item, 'text') and isinstance(content_item.text, str):
                    # Workaround: TextContent containing string representation 'b\'...\''
                    if content_item.text.startswith("b'") and content_item.text.endswith("'"):
                        try:
                            # Use ast.literal_eval to safely convert the string 'b\'...\'' back to bytes
                            evaluated_content = ast.literal_eval(content_item.text)
                            if isinstance(evaluated_content, bytes):
                                pdf_bytes_content = evaluated_content
                                print("Extracted PDF bytes from TEXT (evaluated string literal)")
                            else:
                                logging.error(f"ast.literal_eval did not return bytes for PDF content, got {type(evaluated_content)}")
                                pdf_bytes_content = b"Error: Failed to evaluate PDF string as bytes"
                        except (ValueError, SyntaxError) as e:
                            logging.error(f"Failed to evaluate PDF string literal: {e}\nString was: {content_item.text[0:100]}") # Log part of the string
                            pdf_bytes_content = b"Error: Invalid PDF string format"
                    else:
                        # It's a string but not the expected b'...' format - this shouldn't happen for PDF
                        logging.warning(f"PDF content received as unexpected string format: {content_item.text[0:100]}...")
                        pdf_bytes_content = b"Error: Unexpected PDF string format"
                elif hasattr(content_item, 'text') and isinstance(content_item.text, bytes):
                    # If somehow it's already bytes in TextContent
                    pdf_bytes_content = content_item.text
                    print("Extracted PDF bytes from TEXT (was already bytes)")
                else:
                    logging.warning(f"PDF content item is neither Blob nor Text, or has unexpected type: {type(content_item)}")
        
        # --- ADD LOGGING AFTER EXTRACTION ---
        print("\n--- Debugging Extracted PDF Bytes ---")
        print(f"Type of pdf_bytes_content: {type(pdf_bytes_content)}")
        print(f"Extracted bytes preview: {pdf_bytes_content[:30]}") # Show first 30 bytes
        print("----------------------------------\n")
        # --- END LOGGING ---
        
        
        # Save to DB (value, report_data, pdf_b64)
        pdf_b64 = base64.b64encode(pdf_bytes_content).decode("ascii")
        try:
            await self.call_tool("save_report", {
                "value": value,
                "report_data": expanded,
                "pdf_b64": pdf_b64
            })
        except Exception as db_error:
            logging.error(f"Database insert error: {db_error}")

        return {
            "report": report_text,
            "pdf_bytes": pdf_bytes_content
        }

    async def cleanup(self):
        """ Clean up resources """
        await self._stack.aclose()



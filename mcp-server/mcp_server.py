from mcp.server.fastmcp import FastMCP 
import httpx
import asyncpg
import openai
import io
from reportlab.pdfgen import canvas
import os
from dotenv import load_dotenv
import markdown2
from weasyprint import HTML
import base64, json

load_dotenv()

mcp = FastMCP(name="cybersec-mcp-server")


@mcp.tool()
async def save_report(value: str, report_data: dict, pdf_b64: str) -> str:
    """Save the value or name of the URL/IP/Archive analyzed, the report_data (expanded dict ingested by LLM) 
        and the entire augmented report in PDF bytes outputted by the LLM, all in the database.

    Args:
        value: The name of the URL/IP/Archive analyzed.
        report_data: the VirusTotal report and AbuseIPDB or WHOIS report joined.
        pdf_b64: PDF bytes encoded in Base64 to decode and save as raw bytes.
    """
    pdf_bytes = base64.b64decode(pdf_b64)
    conn = await asyncpg.connect(os.getenv("DATABASE_URL"))
    await conn.execute(
        """
        INSERT INTO reports (value, report_data, pdf_content)
        VALUES ($1, $2::jsonb, $3)
        """,
        value,
        json.dumps(report_data),
        pdf_bytes
    )
    await conn.close()
    return "ok"

@mcp.tool()
async def whois_lookup(domain: str) -> dict:
    """Get all WHOIS fresh info related to the given domain.

    Args:
        domain: The domain to do the WHOIS lookup.
    """
    async with httpx.AsyncClient(timeout=60.0) as client:
        try:    
            resp = await client.get(
                "https://www.whoisxmlapi.com/whoisserver/WhoisService",
                params={"apiKey": os.getenv("WHOIS_API_KEY"),
                        "domainName": domain,
                        "outputFormat": "JSON",
                        "hardRefresh": 1}
            )
            data = resp.json()
            return data
        except httpx.TimeoutException:
            return {"error": "WHOIS API request timed out"}
        except Exception as e:
            return {"error": f"WHOIS API error: {str(e)}"}

@mcp.tool()
async def abuse_ipdb_lookup(ip: str) -> dict:
    """Get all AbuseIPDB info related to an IP Address"

    Args:
        ip: The ip to do the AbuseIPDB lookup.
    """
    resp = await httpx.get(
        "https://api.abuseipdb.com/api/v2/check",
        headers={"Key": os.getenv("ABUSEIPDB_API_KEY")},
        params={"ipAddress": ip, "maxAgeInDays": 90}
    )
    return resp.json()["data"]

@mcp.tool()
def export_pdf(report_text: str) -> bytes:
    """Convert to a PDF output a report in natural language.

    Args:
        report_text: The text to be converted.
    """
    # Convert markdown to HTML (with sane defaults)
    html = markdown2.markdown(report_text, extras=["fenced-code-blocks"])
    # WeasyPrint will honor <h1>…<ul>…<ol>… perfectly
    pdf_bytes = HTML(string=html).write_pdf()
    return pdf_bytes

if __name__ == "__main__":
    # Start an stdio-based MCP server
    mcp.run()
        
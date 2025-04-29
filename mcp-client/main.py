from fastapi import FastAPI, HTTPException
import httpx
import os
import base64
import asyncio
import time
from dotenv import load_dotenv
from mcp_client import MCPClient

load_dotenv()
app = FastAPI()

mcp_client = MCPClient()

@app.on_event("startup")
async def startup():
    await mcp_client.connect_to_server()

@app.on_event("shutdown")
async def shutdown():
    await mcp_client.cleanup() 

# URL example
@app.post("/analyze/")
async def analyze(payload: dict):
    # 1. Llamada 1 a VirusTotal (URL)
    async with httpx.AsyncClient() as client:
        resp1 = await client.post(
            "https://www.virustotal.com/api/v3/urls",
            data={"url": payload["value"]},
            headers={"x-apikey": os.getenv("VT_API_KEY"),
                     "accept": "application/json",
                     "content-type": "application/x-www-form-urlencoded"}
        )
    if resp1.status_code != 200:
        raise HTTPException(502, "Error llamada 1 en VirusTotal")

    # 2. Llamada 2 a VirusTotal (URL)
    url_id = resp1.json()["data"]["id"]
    # TEST PRINT
    print(f"RESP1: {resp1.json()}\n")
    print(f"URL_ID: {url_id}\n")

    async with httpx.AsyncClient() as client:
        resp2 = await client.get(
            f"https://www.virustotal.com/api/v3/analyses/{url_id}",
            headers={"x-apikey": os.getenv("VT_API_KEY"),
                     "accept": "application/json"}
        )
    if resp2.status_code != 200:
        raise HTTPException(502, "Error llamada 2 en VirusTotal")
    raw_report = resp2.json()

    # TEST PRINT
    print(f"RAW_REPORT: {raw_report}\n")
    print(f"VALUE: {payload["value"]}\n")

    # Poll for queued requests
    max_retries = 15
    base_delay = 2
    max_total_wait = 60
    current_attempt = 0
    total_wait_time = 0

    while (raw_report.get('data', {}).get('attributes', {}).get('status') == 'queued' and current_attempt < max_retries \
           and total_wait_time < max_total_wait):

        current_delay = min(base_delay * (2 ** current_attempt), 10)

        if total_wait_time + current_delay > max_total_wait:
            current_delay = max_total_wait - total_wait_time
        print(f"Waiting {current_delay}s before retry {current_attempt + 1}...")
        await asyncio.sleep(current_delay)
        current_attempt += 1
        async with httpx.AsyncClient() as client:
            resp2 = await client.get(
                f"https://www.virustotal.com/api/v3/analyses/{url_id}",
                headers={"x-apikey": os.getenv("VT_API_KEY"),
                        "accept": "application/json"}
            )
        if resp2.status_code == 200:
            raw_report = resp2.json()
            print(f"RETRY {current_attempt} - Status: {raw_report.get('data', {}).get('attributes', {}).get('status')}")
        else:
            break
    
    if raw_report.get('data', {}).get('attributes', {}).get('status') ==  'queued':
        print(f"WARNING: Analysis still queued after {total_wait_time}s of waiting. Proceeding with partial data.")

    # 3. Enriquecimiento profundo MCP
    result = await mcp_client.augment_report(raw_report, payload["value"])
    
    # --- ADD LOGGING HERE ---
    print("\n--- Debugging Result in main.py ---")
    print(f"Type of result['pdf_bytes']: {type(result['pdf_bytes'])}")
    print(f"Bytes preview before base64: {result['pdf_bytes'][:30]}")
    print("----------------------------------\n")
    # --- END LOGGING ---
    
    pdf_base64 = base64.b64encode(result["pdf_bytes"]).decode('ascii')
    
    return {
        "report": result["report"],
        "pdf_base64": pdf_base64
    }



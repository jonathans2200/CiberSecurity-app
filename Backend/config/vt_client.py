import base64
import os
import aiohttp


from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("VT_KEY")

API_KEY = api_key 
HEADERS = {"x-apikey": API_KEY}

async def analyze_ip(ip: str):
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://www.virustotal.com/api/v3/ip_addresses/{ip}", headers=HEADERS) as resp:
            data = await resp.json()
            if resp.status == 404:
                return {"message": "Esta IP no ha sido analizada aún por VirusTotal."}
            return data

def encode_url_to_id(url: str):
    url_bytes = url.encode("utf-8")
    b64_bytes = base64.urlsafe_b64encode(url_bytes)
    return b64_bytes.decode("utf-8").strip("=")

async def analyze_url(url: str):
    async with aiohttp.ClientSession() as session:
      
        async with session.post(
            "https://www.virustotal.com/api/v3/urls",
            headers=HEADERS,
            data={"url": url}
        ) as post_resp:
            post_data = await post_resp.json()

      
        encoded_url_id = encode_url_to_id(url)

        async with session.get(
            f"https://www.virustotal.com/api/v3/urls/{encoded_url_id}",
            headers=HEADERS
        ) as get_resp:
            return await get_resp.json()

async def analyze_file(file_bytes: bytes, filename: str):
    async with aiohttp.ClientSession() as session:
       
        data = aiohttp.FormData()
        data.add_field("file", file_bytes, filename=filename)

        async with session.post(
            "https://www.virustotal.com/api/v3/files",
            headers=HEADERS,
            data=data
        ) as post_response:
            if post_response.status != 200:
                return {
                    "error": {
                        "status": post_response.status,
                        "message": await post_response.text()
                    }
                }
            post_data = await post_response.json()
            analysis_id = post_data["data"]["id"]

      
        async with session.get(
            f"https://www.virustotal.com/api/v3/analyses/{analysis_id}",
            headers=HEADERS
        ) as get_response:
            return await get_response.json()
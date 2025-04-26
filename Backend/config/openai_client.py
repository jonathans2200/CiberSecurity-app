
import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_KEY")
client = OpenAI(
  api_key=api_key
)
async def generate_report(vt_response:dict)->str:

    prompt = f"""
    Analiza el siguiente reporte de seguridad de VirusTotal y genera un informe sencillo para un usuario no técnico. 
    Si detectas que el archivo, IP o URL tiene amenazas, sugiere medidas de seguridad para mitigar riesgos.

    Reporte de VirusTotal:
    \"\"\"{vt_response}\"\"\"
   
    Por favor, proporciona:
    - Un resumen general del estado.
    - Principales riesgos encontrados (si los hay).
    - Recomendaciones de seguridad si aplica.
     
       """
    completion = client.chat.completions.create(
  model="gpt-4o-mini",
  store=True,
  messages=[
    {"role": "user", "content": prompt}
  ]
)

   
    return completion.choices[0].message.content



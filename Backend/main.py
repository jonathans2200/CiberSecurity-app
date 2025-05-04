from typing import Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Query,Depends
from fastapi.encoders import jsonable_encoder
from config.vt_client import analyze_ip, analyze_url, analyze_file
from config.openai_client import generate_report
from entity.Log import save_log_async

import asyncio
import aiohttp
from config.auth import require_roles
from entity.Log import Log
from config.db import SessionLocal, engine, Base
from datetime import datetime
from sqlalchemy.orm import Session
Base.metadata.create_all(bind=engine)
from dotenv import load_dotenv
from fastapi.middleware.cors import CORSMiddleware 
load_dotenv() 
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "http://localhost:8002"],  # Solo tu frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/logs")
def get_logs(
    user= require_roles("SecurityOps"),
    type: Optional[str] = Query(None, description="Filtrar por tipo: ip, url, file"),
    fecha_inicio: Optional[datetime] = Query(None, description="Fecha desde (YYYY-MM-DD)"),
    fecha_fin: Optional[datetime] = Query(None, description="Fecha hasta (YYYY-MM-DD)"),
    db: Session = Depends(get_db)
):
    query = db.query(Log)

    if type:
        query = query.filter(Log.type == type)

    if fecha_inicio:
        query = query.filter(Log.created_at >= fecha_inicio)

    if fecha_fin:
        query = query.filter(Log.created_at <= fecha_fin)

    logs = query.order_by(Log.created_at.desc()).all()

    return jsonable_encoder(logs)






@app.post("/analyze")
async def analyze(
  type:Optional[str],
  value:Optional[str]=Query(None, description="IP o URL a analizar"),
  file: Optional[UploadFile] = File(None),
  user= require_roles("SecurityOps")
):
    vt_response = None

    if type == "url":
        vt_response = await analyze_url(value)
       
    elif type == "ip":
        vt_response = await analyze_ip(value)
    elif type == "file":
        contents = await file.read()
        vt_response = await analyze_file(contents, file.filename)
        value= file.filename
    else:
        raise HTTPException(status_code=400, detail="Tipo no válido. Usa: url, ip o file")
    
    report = await generate_report(vt_response)
    asyncio.create_task(save_log_async(type,value, vt_response, report))
    
    
    
    return {
        "type": type,
        "value": value,
        "openai_response":report,
        "virustotal_report": vt_response}





@app.post("/advanced-analysis")
async def advanced_analysis(
  payload: dict,
  user= require_roles("UserPremium")
):
    """Recibe un payload con la URL a analizar.

    Args:
        payload: json={"value": "url_a_analizar"}
    """
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json"
    }
    async with aiohttp.ClientSession() as session:
        async with session.post(
            "http://fastapi:8000/analyze",
            headers=headers,
            json=payload
        ) as resp:
            response = await resp.json()
            print(response)
            return response


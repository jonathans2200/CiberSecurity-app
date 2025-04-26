from typing import Optional
from fastapi import FastAPI, HTTPException, UploadFile, File, Query,Depends
from fastapi.encoders import jsonable_encoder
from config.vt_client import analyze_ip, analyze_url, analyze_file
from config.openai_client import generate_report
from entity.Log import save_log_async
from config.auth import get_current_user
import asyncio
from entity.Log import Log
from config.db import SessionLocal, engine, Base
from datetime import datetime
from sqlalchemy.orm import Session
Base.metadata.create_all(bind=engine)
from dotenv import load_dotenv
load_dotenv() 
app = FastAPI()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/logs")
def get_logs(
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



# @app.post("/analyze")
# async def analyze(type:str, value:Optional[str]=Query(None, description="IP o URL a analizar"),file: Optional[UploadFile] = File(None)):
#     vt_response = None

#     if type == "url":
#         vt_response = await analyze_url(value)
       
#     elif type == "ip":
#         vt_response = await analyze_ip(value)
#     elif type == "file":
#         contents = await file.read()
#         vt_response = await analyze_file(contents, file.filename)
#         value= file.filename
#     else:
#         raise HTTPException(status_code=400, detail="Tipo no válido. Usa: url, ip o file")
    
#     report = await generate_report(vt_response)
#     asyncio.create_task(save_log_async(type,value, vt_response, report))
    
    
    
#     return {"virustotal_report": vt_response}




@app.post("/analyze")
async def analyze(type:str, value:Optional[str]=Query(None, description="IP o URL a analizar"),file: Optional[UploadFile] = File(None)):
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



@app.get("/profile")
def protected_route(user: dict = Depends(get_current_user)):
    return {
        "message": "Token válido",
        "user": user
    }
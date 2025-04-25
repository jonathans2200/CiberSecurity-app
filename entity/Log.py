from sqlalchemy import JSON, Column, Integer, String, DateTime

from sqlalchemy.sql import func
from config.db import  Base, SessionLocal
from sqlalchemy.orm import Session


class Log(Base):
    __tablename__ = "logs"

    id = Column(Integer, primary_key=True, index=True)
    vt_response = Column(JSON) 
    openai_response = Column(String)  
    type = Column(String)  
    value = Column(String) 
    created_at = Column(DateTime, server_default=func.now())


async def save_log_async(type,value, vt_response, openai_response):
    db: Session = SessionLocal()
    db_log = Log(
        type=type,
        value=value,
        vt_response=vt_response,  
        openai_response=openai_response 
    )
    db.add(db_log)
    db.commit()
    db.close()
from fastapi import APIRouter, Depends, HTTPException, UploadFile, Form
from sqlalchemy.orm import Session
from typing import List
import service, models, schemas
from database import SessionLocal, engine

models.Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get('/users/')
async def get_users(db: Session = Depends(get_db)):
    return await service.get_users(db)

@router.get('/users/id')
async def get_users_id( id: int , db: Session = Depends(get_db)):
    return await service.get_users_id(db , id)

@router.post('/users/')
async def post_users( id: int, name: str, email: str, phone: str, password: str , db: Session = Depends(get_db)):
    return await service.post_users(db , id, name, email, phone, password)

@router.put('/users/id/')
async def put_users_id( id: str, name: str, email: str, phone: str, password: str , db: Session = Depends(get_db)):
    return await service.put_users_id(db , id, name, email, phone, password)

@router.delete('/users/id')
async def delete_users_id( id: int , db: Session = Depends(get_db)):
    return await service.delete_users_id(db , id)


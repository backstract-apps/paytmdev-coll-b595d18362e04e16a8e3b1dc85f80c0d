from sqlalchemy.orm import Session
from typing import List
from fastapi import UploadFile
import models, schemas
import boto3

from pathlib import Path

async def get_users(db: Session):

    users_all = db.query(models.Users).all()
    res = {
        'users_all': users_all,
    }
    return res

async def get_users_id(db: Session, id: int):

    users_one = db.query(models.Users).filter(models.Users.id == id).first()
    res = {
        'users_one': users_one,
    }
    return res

async def post_users(db: Session, id: int, name: str, email: str, phone: str, password: str):


    user_name: str = name

    res = {
        'fullname': name,
    }
    return res

async def put_users_id(db: Session, id: str, name: str, email: str, phone: str, password: str):

    users_edited_record = db.query(models.Users).filter(models.Users.id == id).first()
    for key, value in {'id': id, 'name': name, 'email': email, 'phone': phone, 'password': password}.items():
          setattr(users_edited_record, key, value)
    db.commit()
    db.refresh(users_edited_record)
    users_edited_record = users_edited_record

    res = {
        'users_edited_record': users_edited_record,
    }
    return res

async def delete_users_id(db: Session, id: int):

    users_deleted = None
    record_to_delete = db.query(models.Users).filter(models.Users.id == id).first()

    if record_to_delete:
          db.delete(record_to_delete)
          db.commit()
          users_deleted = record_to_delete
    res = {
        'users_deleted': users_deleted,
    }
    return res


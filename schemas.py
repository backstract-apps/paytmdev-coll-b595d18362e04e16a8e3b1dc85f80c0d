from pydantic import BaseModel

import datetime

import uuid

from typing import Any, Dict, List, Tuple

class Users(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    password: str


class ReadUsers(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    password: str
    class Config:
        from_attributes = True



import datetime

from typing import Optional
from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: int

class ProductUpdate(BaseModel):
    name: Optional[str] = None
    price: Optional[int] = None

class ProductResponse(ProductCreate):
    id: int
    created_at: datetime.datetime
    updated_at: datetime.datetime

    class Config:
        from_attributes = True
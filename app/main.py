from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from typing import List
from app.database import get_db
from app.models import Product

app = FastAPI()

class ProductCreate(BaseModel):
    name: str
    sku: str
    quantity: int
    price: float

class ProductRead(BaseModel):
    id: int
    name: str
    sku: str
    quantity: int
    price: float
    class Config:
        orm_mode = True

@app.post("/products/", response_model=ProductRead)
async def add_product(product: ProductCreate, db: AsyncSession = Depends(get_db)):
    # Implement async logic to add a product
    pass

@app.get("/products/", response_model=List[ProductRead])
async def list_products(db: AsyncSession = Depends(get_db)):
    # Implement async logic to fetch all products
    pass

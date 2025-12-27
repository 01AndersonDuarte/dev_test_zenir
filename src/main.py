from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy import exc

from .database import Base, engine, get_session
from .models import Products
from .schemas import ProductCreate, ProductResponse

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Dev Test Zenir", version="1.0.0")

@app.get("/health")
def health_route():
    return {"Status": "Is running"}

@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate, db=Depends(get_session)) -> ProductResponse:
    new_product = Products(name=product.name, price=product.price)
    
    try:
        db.add(new_product)
        db.commit()
        db.refresh(new_product)
        return new_product

    except exc.IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product with this name already exists",
        )
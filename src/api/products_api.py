from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy import exc

from src.database import get_session
from src.schemas.products_schema import ProductCreate, ProductResponse, ProductUpdate
from src.models.products_model import Products
from src.crud.products_crud import ProductsRepository

router = APIRouter(prefix="/products", tags=["products"])

@router.post("/", response_model=ProductResponse)
def create_product(product: ProductCreate, db=Depends(get_session)) -> ProductResponse:
    products_repository = ProductsRepository(db)
    new_product = Products(name=product.name, price=product.price)
    
    try:
        return products_repository.create(new_product)

    except exc.IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product with this name already exists",
        )

@router.get("/{product_id}", response_model=ProductResponse)
def get_product(product_id: int, db=Depends(get_session)) -> ProductResponse:
    products_repository = ProductsRepository(db)
    product = products_repository.get_by_id(product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    return product

@router.get("/", response_model=list[ProductResponse])
def list_products(db=Depends(get_session)) -> list[ProductResponse]:
    products_repository = ProductsRepository(db)

    return products_repository.list_all()

@router.patch("/{product_id}", response_model=ProductResponse)
def update_product(product_id: int, product: ProductUpdate, db=Depends(get_session)) -> ProductResponse:
    products_repository = ProductsRepository(db)
    existing_product = products_repository.get_by_id(product_id)

    if not existing_product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    if product.name is not None:
        existing_product.name = product.name

    if product.price is not None:  
        existing_product.price = product.price

    try:
        return products_repository.update(existing_product)

    except exc.IntegrityError:
        db.rollback()

        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Product with this name already exists",
        )

@router.delete("/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int, db=Depends(get_session)):
    products_repository = ProductsRepository(db)
    product = products_repository.get_by_id(product_id)

    if not product:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Product not found",
        )

    products_repository.delete(product)
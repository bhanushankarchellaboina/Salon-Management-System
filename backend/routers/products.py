from fastapi import FastAPI, APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from db.database import get_db
from db import db_models
from models import products

router = APIRouter(prefix="/products", tags=["Products"])


@router.get("/", response_model=list[products.Product])
def get_products(db: Session = Depends(get_db)):
    return db.query(db_models.Product).all()


@router.post("/", response_model=products.Product)
def add_product(product: products.Product,
                db: Session = Depends(get_db)):
    new_product = db_models.Product(**product.model_dump())

    db.add(new_product)

    db.commit()

    db.refresh(new_product)

    return new_product


@router.get("/{product_id}", response_model=products.Product)
def get_product(product_id: int,
                db: Session = Depends(get_db)):
    return db.query(db_models.Product) \
        .filter(db_models.Product.id == product_id) \
        .first()


@router.delete("/{product_id}")
def delete_product(product_id: int,
                   db: Session = Depends(get_db)):
    product = db.query(db_models.Product) \
        .filter(db_models.Product.id == product_id) \
        .first()

    db.delete(product)

    db.commit()

    return {"message": "Product Deleted Successfully"}


@router.put("/{product_id}", response_model=products.Product)
def update_product(
        product_id: int,
        updated_product: products.Product,
        db: Session = Depends(get_db)
):
    product = (
        db.query(db_models.Product)
        .filter(db_models.Product.id == product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found"
        )

    product.name = updated_product.name
    product.category = updated_product.category
    product.description = updated_product.description
    product.brand = updated_product.brand
    product.price = updated_product.price
    product.image = updated_product.image

    db.commit()
    db.refresh(product)

    return product

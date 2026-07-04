from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func

from db import db_models
from db.database import get_db
from models.items import Item, CategoryCard

router = APIRouter(prefix='/items', tags=['items'])


@router.get("/")
def get_items(db: Session = Depends(get_db)):
    db_items = db.query(db_models.Item).order_by(db_models.Item.price).all()
    return db_items




@router.get("/categories", response_model=list[CategoryCard])
def get_categories(db: Session = Depends(get_db)):

    categories = (
        db.query(
            db_models.Item.category,
            func.min(db_models.Item.price).label("starting_price"),
            func.min(db_models.Item.image).label("image")
        )
        .group_by(db_models.Item.category)
        .all()
    )

    return [
        {
            "category": c.category,
            "image": c.image,
            "starting_price": c.starting_price
        }
        for c in categories
    ]


@router.get("/category/{category}")
def get_services_by_category(category: str, db: Session = Depends(get_db)):

    services = (
        db.query(db_models.Item)
        .filter(db_models.Item.category == category)
        .all()
    )

    return services



@router.get("/{item_id}")
def get_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(db_models.Item).filter(db_models.Item.id == item_id).first()
    return db_item


@router.post("/")
def post_item(item: Item, db: Session = Depends(get_db)):
    db.add(db_models.Item(**item.model_dump()))
    db.commit()
    return item


@router.put("/{item_id}")
def update_item(item_id: int, item: Item, db: Session = Depends(get_db)):
    db_items = db.query(db_models.Item).filter(db_models.Item.id == item_id).first()
    if db_items:
        db_items.id = item.id
        db_items.name = item.name
        db_items.category = item.category
        db_items.price = item.price
        db_items.image = item.image
        # db_items.duration = item.Duration
        db.commit()
    else:
        return "no item found"


@router.delete("/{item_id}")
def delete_item(item_id=int, db: Session = Depends(get_db)):
    db_items = db.query(db_models.Item).filter(db_models.Item.id == item_id).first()
    if db_items:
        db.delete(db_items)
        db.commit()
        return "product deleted successfully"
    else:
        return "product not found"



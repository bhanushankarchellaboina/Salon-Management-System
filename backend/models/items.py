from pydantic import BaseModel


class Item(BaseModel):
    id: int
    name: str
    category: str
    price: int
    image: str
    # Duration: str


class CategoryCard(BaseModel):
    category: str
    image: str
    starting_price: int

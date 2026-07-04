from pydantic import BaseModel


class Product(BaseModel):
    id: int
    name: str
    category: str
    description: str
    brand: str
    price: int
    image: str

class config:
    from_attributes = True
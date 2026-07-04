from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class Item(Base):
    __tablename__ = "item"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    category = Column(String)
    price = Column(Integer)
    image = Column(String)
    # Duration = Column(String)


class Product(Base):
    __tablename__ = "Products"

    id = Column(Integer,primary_key=True,index=True)
    name = Column(String, nullable=False)
    category = Column(String, nullable=False)
    description = Column(String,nullable=False)
    brand = Column(String,nullable=False)
    price = Column(Integer,nullable=False)
    image = Column(String)
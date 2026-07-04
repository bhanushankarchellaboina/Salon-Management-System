from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import db_models
from db.database import engine
from routers import items
from routers import products

db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173" ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(products.router)
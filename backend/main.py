from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from db import db_models
from db.database import engine
from routers import items, products

# Create tables
db_models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # We'll restrict this after deploying the frontend
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(items.router)
app.include_router(products.router)
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

db_url = "postgresql://postgres:12345@localhost:5432/beauty_saloon"
engine = create_engine(db_url)

session = sessionmaker(
    autoflush=False,
    bind=engine
)


def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

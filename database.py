from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "postgresql://postgres:ErBNpjrg9bP8UasmGaQV@containers-us-west-139.railway.app:6575/railway"

engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autoflush=False, autocommit=False, bind=engine)
Base = declarative_base()

def get_db():
    db = localSession()
    try:
        yield db
    finally:
        db.close()
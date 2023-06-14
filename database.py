from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

DATABASE_URL = "mysql://root:IVCUMVU5UrJwZHybXrX8@containers-us-west-198.railway.app:6960/railway"

engine = create_engine(DATABASE_URL)
localSession = sessionmaker(autoflush=False, autoCommit=False, bind=engine)
Base = declarative_base()

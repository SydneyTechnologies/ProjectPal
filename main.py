from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import tables
from database import engine
from endpoints import users

tables.BaseTable.metadata.create_all(bind=engine)

DESCRIPTION = "Welcome to Project Pal! Showcase projects, create stunning portfolios. Add details, images, demos.  Effortlessly showcase your work. Join Project Pal today!"
app = FastAPI(title="ProjectPal Api", description=DESCRIPTION)
app.add_middleware(
    CORSMiddleware, 
    allow_origins = ["*"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users.router)
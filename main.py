from fastapi import FastAPI
from endpoints import users

DESCRIPTION = "Welcome to Project Pal! Showcase projects, create stunning portfolios. Add details, images, demos.  Effortlessly showcase your work. Join Project Pal today!"
app = FastAPI(title="ProjectPal Api", description=DESCRIPTION)

app.include_router(users.router)
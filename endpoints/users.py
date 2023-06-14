from fastapi import APIRouter
router = APIRouter()

@router.get("/register", tags=["Auth"], summary="Register a new user to Project Pal")
def register():
    return "This endpoint registers a new user"


@router.get("/login", tags=["Auth"], summary="Login user to Project Pal")
def login():
    return "This endpoint registers a new user"
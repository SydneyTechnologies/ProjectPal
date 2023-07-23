from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm
from schema import CreateUser, UserBase
from database import get_db
import crud, utils, tables
router = APIRouter()


@router.post("/register", tags=["Auth"], summary="Register a new user to Project Pal")
def register(userData: CreateUser, db = Depends(get_db)):
    password = userData.password
    password = utils.hashPassword(password=password)
    userData.password = password

    #create a new database user 
    try: 
        new_user = tables.User(**userData.dict())
        db_user = crud.add_to_db(dbObject=new_user, db=db)
        if not db_user: 
            raise HTTPException(status_code=status.HTTP_417_EXPECTATION_FAILED, detail="Failed to register user")
        return {"status":"Registration Successful"}
    except Exception as error:
        raise error
        


@router.post("/login", tags=["Auth"], summary="Login user to Project Pal")
def login(formData: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm), db = Depends(get_db)):
    email = formData.username
    password = formData.password

    db_user = crud.get_user(email=email, db=db)
    if db_user is None: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    
    is_password_valid = utils.validatePassword(entry=password, password=db_user.password)
    if is_password_valid: 
        return {"access-token": utils.generateAccessToken(email=db_user.email), "token_type": "bearer"}
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Incorrect Credentials")


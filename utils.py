import bcrypt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt;
from database import get_db
import crud


auth_scheme = OAuth2PasswordBearer(tokenUrl="login")
SECRET_KEY = "4b7861d25c5400871418379f71bf262eef86ccc32a90f2bb95aaf195306e4abf"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 20


def hashPassword(password: str):
    encoded_password = password.encode("utf-8")
    hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
    return hashed_password


def validatePassword(entry: str, password: str):
    encoded_entry = entry.encode("utf-8")
    if bcrypt.checkpw(encoded_entry, password):
        return True
    else:
        return False
    
def generateAccessToken(email: str):
    expiration_time = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    tokenData = {"email":email, "expiration": expiration_time.isoformat()}
    encoded_jwt = jwt.encode(tokenData, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def get_current_user(token:str = Depends(auth_scheme), db = Depends(get_db)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    print(token)
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email: str = payload.get("email")
        print(payload)
        if email is None:
            raise credentials_exception
    except JWTError:
        # email: str = payload.get("email")
        print(token)
        raise credentials_exception
    user = crud.get_user(email=email, db=db)
    if user is None:
        raise credentials_exception
    return user
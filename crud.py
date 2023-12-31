from database import localSession
from fastapi import Depends
from sqlalchemy.orm import Session
from sqlalchemy import update
import tables
import schema


def get_user(email:str, db: Session)->tables.User:
    user = db.query(tables.User).filter(tables.User.email == email).first()
    return user


# def update_user(user: tables.User, userData: schema.UpdateUser, db: Session):
#     # first remove non values 
#     updates = {}
#     for key, value in userData.dict().items():
#         if value != None:
#             updates[key] = value
#     if user: 
#         update_query = update(tables.User).where(tables.User.email == user.email).values(updates)
#         db.execute(update_query)
#         db.commit()
#         db.refresh(user)
#     return user

# def update_poll(poll: tables.Poll, pollData: schema.UpdateUser, db: Session):
#     # first remove non values 
#     updates = {}
#     for key, value in pollData.dict().items():
#         if value != None:
#             updates[key] = value

#     update_query = update(tables.Poll).where(tables.Poll.id == poll.id).values(updates)
#     db.execute(update_query)
#     db.commit()
#     db.refresh(poll)
#     return poll


def delete_from_db(dbObject: any, db: Session )-> bool:
    if dbObject:
        db.delete(dbObject)
        db.commit()
        return True
    
    return False
                


def add_to_db(dbObject: any, db: Session)->tables.Base:
    if dbObject:
        db.add(dbObject)
        db.commit()
        db.refresh(dbObject)
    return dbObject



def get_db_objects(object: tables.Base,  db: Session)->list[tables.Base]:
    results = db.query(object).all()
    return results
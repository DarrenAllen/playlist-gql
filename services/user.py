from fastapi import Depends, HTTPException, status
from models.user import Users
from sqlmodel import Session, select
from database import get_session
def read_users():
    db = next(get_session())
    users = db.exec(select(Users)).all()
    return users
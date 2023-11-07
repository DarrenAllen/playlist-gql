from fastapi import Depends, HTTPException, status
from models.idea import Ideas
from sqlmodel import Session, select
from database import get_session
def read_ideas():
    db = next(get_session())
    ideas = db.exec(select(Ideas)).all()
    return ideas
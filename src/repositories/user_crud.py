from datetime import datetime

from sqlalchemy.orm import Session

from src.models import User
from src.schemas import UserCreate


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(User).offset(skip).limit(limit).all()


def create_user(db: Session, user: UserCreate):
    db_user = User(**user.model_dump()) # Workout(name=workout.name, description=workout.description)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

from datetime import datetime

from sqlalchemy.orm import Session

from src.models import Exercise
from src.schemas import ExerciseCreate


def get_exercise(db: Session,exercise_id: int):
    return db.query(Exercise).filter(Exercise.id == exercise_id).first()


def get_exercises(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Exercise).offset(skip).limit(limit).all()


def create_exercise(db: Session, exercise: ExerciseCreate):
    db_exercise = Exercise(**exercise.model_dump()) # Workout(name=workout.name, description=workout.description)
    db.add(db_exercise)
    db.commit()
    db.refresh(db_exercise)
    return db_exercise
from sqlalchemy.orm import Session

from src.models import Workout
from src.schemas import WorkoutCreate


def get_workout(db: Session, workout_id: int):
    return db.query(Workout).filter(Workout.id == workout_id).first()


def get_workouts(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Workout).offset(skip).limit(limit).all()


def create_workout(db: Session, workout: WorkoutCreate):
    db_workout = Workout(**workout.model_dump()) # Workout(name=workout.name, description=workout.description)
    db.add(db_workout)
    db.commit()
    db.refresh(db_workout)
    return db_workout

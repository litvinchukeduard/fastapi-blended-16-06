from datetime import time, timedelta, datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.configuration.database import get_db
from src.repositories import workout_crud

from src.schemas import WorkoutCreate, WorkoutRetrieve

workout_router = APIRouter(prefix="/api/workouts", tags=['workouts'])

# - GET /api/workouts Returns all workouts in the system

# - POST /api/workouts Create a workout in the system
@workout_router.get("/")
async def read_workouts(db: Session = Depends(get_db)):
    return workout_crud.get_workouts(db)

@workout_router.get("/{id}")
async def read_workouts(id: int, db: Session = Depends(get_db)):
    workout_db = workout_crud.get_workout(db, id)
    workout_retrieve = WorkoutRetrieve(**workout_db.__dict__)

    total_calories = 0
    total_time = datetime(year=1970, month=1, day=1) # TODO: find a better way
    for exercise in workout_db.exercises:
        total_calories += exercise.calories

        duration = exercise.duration
        exercise_timedelta = timedelta(hours=duration.hour, minutes=duration.minute, seconds=duration.second)
        total_time += exercise_timedelta

    workout_retrieve.total_calories = total_calories
    workout_retrieve.total_time = total_time.time()
    return workout_retrieve

@workout_router.post("/", response_model=WorkoutRetrieve)
async def create_workout(workout: WorkoutCreate, db: Session = Depends(get_db)):
    return workout_crud.create_workout(db, workout)

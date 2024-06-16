from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.configuration.database import get_db
from src.repositories import exercise_crud

from src.schemas import ExerciseCreate, ExerciseRetrieve

exercise_router = APIRouter(prefix="/api/exercises", tags=['workouts'])

# - GET /api/workouts Returns all workouts in the system

# - POST /api/workouts Create a workout in the system
@exercise_router.get("/")
async def read_exercises(db: Session = Depends(get_db)):
    return exercise_crud.get_exercises(db)

@exercise_router.post("/", response_model=ExerciseRetrieve)
async def create_exercises(exercise: ExerciseCreate, db: Session = Depends(get_db)):
    return exercise_crud.create_exercise(db, exercise)

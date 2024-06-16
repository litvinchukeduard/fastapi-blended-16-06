from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.configuration.database import get_db
from src.repositories import workout_crud

workout_router = APIRouter(prefix="/api/workouts", tags=['workouts'])

# - GET /api/workouts Returns all workouts in the system

# - POST /api/workouts Create a workout in the system
@workout_router.get("/")
async def read_workouts(db: Session = Depends(get_db)):
    return workout_crud.get_workouts(db)

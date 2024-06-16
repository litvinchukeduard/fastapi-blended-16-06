from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.configuration.database import get_db
from src.repositories import user_crud

from src.schemas import UserCreate, UserRetrieve

user_router = APIRouter(prefix="/api/users", tags=['user'])

# - GET /api/workouts Returns all workouts in the system

# - POST /api/workouts Create a workout in the system
@user_router.get("/{id}")
async def read_user_by_id(id: int, db: Session = Depends(get_db)):
    return user_crud.get_user(db, id)

@user_router.post("/", response_model=UserRetrieve) #TODO: use authorization https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#__tabbed_1_1
async def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db, user)

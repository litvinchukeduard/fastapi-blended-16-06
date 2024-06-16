from datetime import time
from pydantic import BaseModel


class WorkoutBase(BaseModel):
    name: str
    description: str


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutRetrieve(WorkoutBase):
    id: int
    total_time: time | None = None
    total_calories: int | None = None

    class Config:
        orm_mode = True

class ExerciseBase(BaseModel):
    name: str
    duration: time
    calories: int


class ExerciseCreate(ExerciseBase):
    pass


class ExerciseRetrieve(ExerciseBase):
    id: int

    class Config:
        orm_mode = True

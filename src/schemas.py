from pydantic import BaseModel


class WorkoutBase(BaseModel):
    name: str
    description: str


class WorkoutCreate(WorkoutBase):
    pass


class WorkoutRetrieve(WorkoutBase):
    id: int

    class Config:
        orm_mode = True

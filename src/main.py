from fastapi import FastAPI
from src.routes.workout_routes import workout_router
from src.routes.exercise_routes import exercise_router

app = FastAPI()

app.include_router(workout_router)
app.include_router(exercise_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
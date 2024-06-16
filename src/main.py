from fastapi import FastAPI
from src.routes.workout_routes import workout_router

app = FastAPI()

app.include_router(workout_router)


@app.get("/")
async def root():
    return {"message": "Hello World!"}
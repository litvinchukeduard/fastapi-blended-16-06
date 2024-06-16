# Фітнес треккер, створити ORM для спотивних вправ
Створити моделі Користувач (Імʼя, вправи), Тренування (користувач, дата, вправи), Вправа (тренування, назва, тривалість в хвилинах, втрачені калорії)

When a user stops workout before the end time, we calculate calories burned

User (id, name, birhtday)

Workout (id, name, description)

Exercise (id, name, duration, calories)

workout_exercise(workout_id, exercise_id, number)

- GET /api/workouts Returns all workouts in the system

- POST /api/workouts Create a workout in the system

- GET /api/exercises Returns all exercises in the system

- POST /api/exercises Create an exercise in the system

- POST /api/signup 

- POST /api/workouts/start

- POST /api/workouts/end

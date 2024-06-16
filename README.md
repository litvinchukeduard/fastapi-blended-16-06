# Фітнес треккер, створити ORM для спотивних вправ
Створити моделі Користувач (Імʼя, вправи), Тренування (користувач, дата, вправи), Вправа (тренування, назва, тривалість в хвилинах, втрачені калорії)

When a user stops workout before the end time, we calculate calories burned

When workout is received, total calories and total time is computed

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

`/api/workouts/{id}/start`

- POST /api/workouts/end

`/api/user_workouts/{id}/end`

User_Workout(user_id, workout_id, start_time, end_time: None)

https://fastapi.tiangolo.com/tutorial/security/oauth2-jwt/#__tabbed_1_1

from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date, Time
from sqlalchemy.orm import relationship
from sqlalchemy.orm import declarative_base

Base = declarative_base()

# User (id, name, birhtday)
# https://docs.sqlalchemy.org/en/13/core/type_basics.html#generic-types
class User(Base):
    __tablename__="users"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    birthday = Column(Date, nullable=False)

class Workout(Base):
    __tablename__= "workout"

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    description = Column(String, nullable=False)

class Exercise(Base):
    __tablename__ = "exercise"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    duration = Column(Time)
    calories = Column(Integer)

class Workout_exercise(Base):
    __tablename__ = 'workout_exercise'

    id = Column(Integer, primary_key=True)
    workout_id = Column(Integer, ForeignKey('workout.id'))
    exercise_id = Column(Integer, ForeignKey('exercise.id'))
    number = Column(Integer)

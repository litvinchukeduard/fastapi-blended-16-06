from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Date
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


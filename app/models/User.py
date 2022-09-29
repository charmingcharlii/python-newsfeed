from app.db import Base
from sqlalchemy import Column, Integer, String

# User class that inherits from the Base class in the db package
class User(Base):
    __tablename__= 'users'
    # uses classes from the sqlalchemy moduole to define columns and give options like nullable 
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)
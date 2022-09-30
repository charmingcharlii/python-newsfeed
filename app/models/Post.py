from datetime import datetime
from email.policy import default
from app.db import Base 
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship

class Post(Base): 
    user = relationship('User')
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    post_url = Column(String(100), nullable=False)
    # references the user table
    user_id = Column(Integer, ForeignKey('users.id'))
    # uses pythons built in datetime module 
    created_at = Column(DateTime, default=datetime.now)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now)
   
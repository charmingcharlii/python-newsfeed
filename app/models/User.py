from app.db import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import validates
import bcrypt 

salt = bcrypt.gensalt()

# User class that inherits from the Base class in the db package
class User(Base):
    __tablename__= 'users'
    # uses classes from the sqlalchemy moduole to define columns and give options like nullable 
    id = Column(Integer, primary_key=True)
    username = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False, unique=True)
    password = Column(String(100), nullable=False)

    @validates('email')
    def validate_email(self, key, email):
        # make sure email address contains @character // will throw error if false 
        assert '@' in email 

        return email 
    
    @validates('password')
    def validate_password(self, key, password):
        assert len(password) > 4

        return bcrypt.hashpw(password.encode('utf-8'), salt) 

    def verify_password(self, password):
        return bcrypt.checkpw(
            password.encode('utf-8'),
            self.password.encode('utf-8')
        )
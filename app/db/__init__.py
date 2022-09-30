from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
from flask import g

load_dotenv()

# conect to the database using env variable 
engine = create_engine(getenv('DB_URL'), echo=True, pool_size=20, max_overflow=0)
# temporary connections for the CRUD operations 
Session = sessionmaker(bind=engine)
# helps map the models to MySQL tables 
Base = declarative_base()

def init_db(app):
  Base.metadata.create_all(engine)

  app.teardown_appcontext(close_db)

# returns a new session connectin object 
def get_db():
  if 'db' not in g:
    # store db connection in app context
    g.db = Session()

  return g.db

def close_db(e=None):
  db = g.pop('db', None)

  if db is not None:
    db.close()
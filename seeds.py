from app.models import User
from app.db import Session, Base, engine

# drop and rebuild tables 
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

# Anytime we want to perform a CRUD operation using SQLAlchemy, we need to establish a temporary session connection with the Session class
db = Session()

# insert users
db.add_all([
  User(username='alesmonde0', email='nwestnedge0@cbc.ca', password='password123'),
  User(username='jwilloughway1', email='rmebes1@sogou.com', password='password123'),
  User(username='iboddam2', email='cstoneman2@last.fm', password='password123'),
  User(username='dstanmer3', email='ihellier3@goo.ne.jp', password='password123'),
  User(username='djiri4', email='gmidgley4@weather.com', password='password123')
])

db.commit()

db.close()
# have to initiate Session, then add_all, then commit, then close
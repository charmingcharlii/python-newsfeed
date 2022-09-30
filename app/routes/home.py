# import the functions Blueprint() and render_template() from Flask
from flask import Blueprint, render_template
from app.models import Post
from app.db import get_db

# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later. This corresponds to using the Router middleware of Express.js.
bp = Blueprint('home', __name__, url_prefix= '/')

# add @bp.route() to turn the function into a route
@bp.route('/')
def index():
  # get all posts
  db = get_db()
  posts = db.query(Post).order_by(Post.created_at.desc()).all()
  # add render_template() to respond with a template instead of a string
  return render_template('homepage.html', posts=posts)

@bp.route('/login')
def login():
  return render_template('login.html')

# this uses a parameter <id>
@bp.route('/post/<id>')
# to capture the value, include it as a function parameter
def single(id):
  #  get single post by id
  db = get_db()
  # This time, we use the filter() method on the connection object to specify the SQL WHERE clause, and we end by using the one() method instead of all()
  post = db.query(Post).filter(Post.id == id).one()

  # render single post template
  return render_template('single-post.html', post=post)

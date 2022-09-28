# import the functions Blueprint() and render_template() from Flask
from flask import Blueprint, render_template

# Blueprint() lets us consolidate routes onto a single bp object that the parent app can register later. This corresponds to using the Router middleware of Express.js.
bp = Blueprint('home', __name__, url_prefix= '/')

# add @bp.route() to turn the function into a route
@bp.route('/')
def index():
    # add render_template() to respond with a template instead of a string
  return render_template('homepage.html')

@bp.route('/login')
def login():
  return render_template('login.html')

# this uses a parameter <id>
@bp.route('/post/<id>')
# to capture the value, include it as a function parameter
def single(id):
  return render_template('single-post.html')

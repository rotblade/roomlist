from flask import render_template
from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Gavin'}
    rooms = [
        {'name': 'Meeting room', 'id': '1', 'size': 20},
        {'name': 'Meeting room', 'id': '2', 'size': 10},
        {'name': 'Meeting room', 'id': '3', 'size': 15},
    ]
    return render_template('index.html', title='Home',
                           user=user, rooms=rooms)

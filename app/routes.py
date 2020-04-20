from flask import render_template

from app import app


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'sam'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'wefwef'
        },
        {
            'author': {'username': 'Alex'},
            'body': 'wefwef'
        },
        {
            'author': {'username': 'Oleg'},
            'body': 'wefwef'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

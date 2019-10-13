from flask import Flask, request, abort, session, redirect, url_for, render_template, make_response, jsonify
from os.path import join, realpath, dirname

app = Flask(__name__)
app.secret_key = b'123456789qwe'


@app.route('/')
def index():
    if 'username' in session:
        return 'logged in as %s' % session.get('username')
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form.get('username')
        return redirect(url_for('index'))
    return '''
        <form method="POST">
            <p><input type="text" name="username">
            <p><input type="submit" name="login">
        </form>
    '''


@app.route('/user/<user_id>')
def user_detail(user_id):
    user_id = user_id
    return {
        "username": "vika",
        "user_id": user_id,
        "nickname": "vika41130",
    }


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('index'))

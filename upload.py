from flask import Flask, request, render_template
from os.path import join, realpath, dirname
import os
import time

app = Flask(__name__)
UPLOAD_PATH = './var/www/upload'


@app.route('/')
def index():
    return 'Index Page'


@app.route('/upload', methods=['GET', 'POST'])
def handle_upload():
    try:
        if request.method == 'POST':
            print('----------', request.files)
            for file in request.files:
                f = request.files[file]
                f.save(os.path.join(UPLOAD_PATH, f.filename))
            return {
                'Success': 1
            }
    except FileNotFoundError:
        print('error happened')
        return {
            'Success': 0
        }

from application import app
from flask import render_template

@app.route('/', methods=["GET"])
def index():
    return 'Casework Style Guide'

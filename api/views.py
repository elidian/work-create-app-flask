from api import app
from flask import Flask, render_template

@app.route('/')
@app.route('/home')
def home():
    return render_template('index.html')

@app.route('/contato')
def contato():
    return 'Contact: None'

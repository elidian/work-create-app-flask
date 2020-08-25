from api import app
from flask import Flask, jsonify, request

@app.route('/')
@app.route('/home')
def home():
    return 'Home page.'

@app.route('/contato')
def contato():
    return 'Contact: None'

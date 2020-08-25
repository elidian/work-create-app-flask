from app import app
from flask import Flask, jsonify

@app.route('/')
@app.rout('/home')
def home():
    return jsonify({'Home page.'})

@app.route('/contato')
def contato():
    return jsonify({'Contact: ', None})

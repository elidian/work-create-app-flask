from flask import Flask

app = Flask(__name__)
app.debug = True
app.secret_key = 'devweb'

from app import views
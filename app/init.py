from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from routes import init_routes
import os

# creates an application that is named after the name of the file
app = Flask(__name__)

app.config["SECRET_KEY"] = "some_dev_key"
# Check if running on Heroku
if 'DATABASE_URL' in os.environ:
  app.config["SQLALCHEMY_DATABASE_URI"] = os.environ['DATABASE_URL']
else:
  # Local PostgreSQL database URL
  app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['LOCAL_DATABASE']

# initializing routes
init_routes(app)

db = SQLAlchemy()


from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from flask_migrate import Migrate


# # creates an application that is named after the name of the file
app = Flask(__name__)

app.config["SECRET_KEY"] = "some_dev_key"

app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL').replace(
        'postgres://', 'postgresql+psycopg2://', 1)

db = SQLAlchemy(app)

# bootstrap database migrate commands
migrate = Migrate(app, db)
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from flask import Flask
import os
from flask_migrate import Migrate


#creates an application that is named after the name of the file
app = Flask(__name__)

# Set the environment config for the app based on the CONFIG_SETTINGS value. Default is DevelopmentConfig
env_config = os.getenv("CONFIG_SETTINGS", "config.DevelopmentConfig")
app.config.from_object(env_config)

# Create SQLAlehcmy instance using the flask application app
db = SQLAlchemy(app)

# bootstrap database migrate commands
migrate = Migrate(app, db)
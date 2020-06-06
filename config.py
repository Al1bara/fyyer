import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres@localhost:5432/fyyer'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

SQLALCHEMY_DATABASE_URI = 'postgres://postgres@localhost:5432/fyyer'
SQLALCHEMY_TRACK_MODIFICATIONS = False
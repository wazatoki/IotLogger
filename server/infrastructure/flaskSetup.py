import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

url_prefix = "/api/"

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/ecmoMonitor.sqlite'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    DEBUG = False
    CSRF_ENABLED = True
    JSON_AS_ASCII = False

app = Flask(__name__,
        static_folder = "../../client/dist/static",
        template_folder = "../../client/dist")
app.config.from_object(Config)
CORS(app, resources={url_prefix + "*": {"origins": "*"}})
ma = Marshmallow(app)
db = SQLAlchemy()
db.init_app(app)
Migrate(app, db)



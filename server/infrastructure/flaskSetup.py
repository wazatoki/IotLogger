import os

from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from gateway import router

url_prefix = "/api/"

db = SQLAlchemy()

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///../db/ecmoMonitor.sqlite'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    DEBUG = True
    CSRF_ENABLED = True

def create_app():
    app = Flask(__name__,
        static_folder = "../../client/dist/static",
        template_folder = "../../client/dist")
    app.config.from_object(Config)
    CORS(app, resources={url_prefix + "*": {"origins": "*"}})
    router.setup_api(app)
    ma = Marshmallow(app)

    db.init_app(app)
    Migrate(app, db)
    
    return app

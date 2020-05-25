import os

from flask import Flask, render_template, jsonify, request
from flask_cors import CORS

from infrastructure import dbSetup

class Config(object):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///db/ecmoMonitor.sqlite3.db'
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-secret-key"
    DEBUG = True
    CSRF_ENABLED = True

def create_app():
    app = Flask(__name__,
        static_folder = "../../client/dist/static",
        template_folder = "../../client/dist")
    app.config.from_object(Config)
    CORS(app, resources={r"/api/*": {"origins": "*"}})
    
    dbSetup.init_db(app)
    return app

    

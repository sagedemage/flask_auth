"""A simple flask web app"""
import logging
import os
from logging.handlers import RotatingFileHandler

import flask_login
from flask import Flask
from flask_bootstrap import Bootstrap5
from flask_wtf.csrf import CSRFProtect

from app.auth import auth
from app.cli import create_database, create_log_folder
from app.context_processors import utility_text_processors
from app.db import db
from app.db.models import User
from app.error_handlers import error_handlers
from app.logging_config import log_con
from app.simple_pages import simple_pages
from app.map import map

login_manager = flask_login.LoginManager()


def create_app():
    """Create and configure an instance of the Flask application."""
    app = Flask(__name__)
    if app.config["ENV"] == "production":
        app.config.from_object("app.config.ProductionConfig")
    elif app.config["ENV"] == "development":
        app.config.from_object("app.config.DevelopmentConfig")
    elif app.config["ENV"] == "testing":
        app.config.from_object("app.config.TestingConfig")

    # login manager
    login_manager.init_app(app)
    login_manager.login_view = "auth.login"

    # CSRF protection of form submissions
    csrf = CSRFProtect(app)
    csrf.exempt(auth)

    # Flask Bootstrap
    bootstrap = Bootstrap5(app)

    # load functions with web interfaces
    app.register_blueprint(simple_pages)
    app.register_blueprint(auth)

    # load functionality without a web interface
    app.register_blueprint(log_con)
    app.register_blueprint(error_handlers)
    app.register_blueprint(map)
    app.context_processor(utility_text_processors)

    # add command function to cli commands
    app.cli.add_command(create_database)
    app.cli.add_command(create_log_folder)
    db.init_app(app)

    # Run once at startup
    return app


@login_manager.user_loader
def user_loader(user_id):
    try:
        return User.query.get(int(user_id))
    except:
        return None

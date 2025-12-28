from flask import Flask
from .core.config import Config
from .db import db


def create_app(config_object: Config = None):
    app = Flask(__name__)

    # Load configuration
    if config_object is None:
        app.config.from_object(Config())
    else:
        app.config.from_object(config_object)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints (API v1)
    from .api.v1.routes.anomaly_model import bp as anomaly_bp
    app.register_blueprint(anomaly_bp, url_prefix="/api/v1/models")

    # Create database tables if they don't exist
    with app.app_context():
        db.create_all()

    return app

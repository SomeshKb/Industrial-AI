from flask import Flask
from routes.model import model_bp
from db import db

app = Flask(__name__)

# SQLite config
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

# Create tables
with app.app_context():
    db.create_all()

# Register routes with /api prefix
app.register_blueprint(model_bp, url_prefix="/api/model")

if __name__ == "__main__":
    app.run(debug=True)

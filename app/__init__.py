from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from dotenv import load_dotenv
import os

db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()

def create_app():
    load_dotenv()

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")  # instance/config.py

    # 명시적으로 환경변수에서 가져와도 OK
    if "SQLALCHEMY_DATABASE_URI" not in app.config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

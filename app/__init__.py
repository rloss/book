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
    app.config.from_pyfile("config.py")

    # DEBUG 설정 없으면 직접 추가해도 됨
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    return app

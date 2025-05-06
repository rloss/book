import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_login import LoginManager
from dotenv import load_dotenv

# ----------------------
# 확장 객체 생성
# ----------------------
db = SQLAlchemy()
migrate = Migrate()
jwt = JWTManager()
login_manager = LoginManager()

# ----------------------
# 앱 팩토리
# ----------------------
def create_app():
    # 환경변수 로딩
    load_dotenv()

    # 앱 인스턴스 생성
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_pyfile("config.py")

    # DB 설정 없을 시 fallback 처리
    if "SQLALCHEMY_DATABASE_URI" not in app.config:
        app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL")

    # 확장 초기화
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)
    login_manager.init_app(app)

    # 로그인 매니저 설정
    login_manager.login_view = "auth.login"  # 로그인 안 된 유저가 접근하면 리디렉트할 라우트 이름
    login_manager.login_message = "로그인이 필요합니다."

    # 사용자 로더 함수 정의
    from app.models.user import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # 라우트 등록
    from app.routes.main import bp as main_bp
    app.register_blueprint(main_bp)

    # 필요 시 auth, group 등 다른 블루프린트도 여기에 추가
    # from app.routes.auth import bp as auth_bp
    # app.register_blueprint(auth_bp)

    return app

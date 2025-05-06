from flask import Blueprint, render_template
from app.models.user import User
from app import db

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    users = User.query.all()
    return render_template("home.html", users=users)

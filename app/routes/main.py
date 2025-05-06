from flask import Blueprint, render_template
from flask_login import current_user
from app.models.post import Post
from app.models.group_book import GroupBook
from app.models.book import Book
from app.models.membership import Membership
from app import db

bp = Blueprint("main", __name__)

@bp.route("/")
def index():
    if current_user.is_authenticated:
        # 1. 최근 작성 글 (최신 5개)
        recent_posts = Post.query.filter_by(user_id=current_user.id) \
                                 .order_by(Post.created_at.desc()) \
                                 .limit(5).all()

        # 2. 내가 속한 그룹의 ID 목록
        memberships = Membership.query.filter_by(user_id=current_user.id).all()
        group_ids = [m.group_id for m in memberships]

        # 3. 현재 읽고 있는 공통 도서 (status = 'active')
        active_books = db.session.query(GroupBook) \
            .filter(GroupBook.group_id.in_(group_ids)) \
            .filter(GroupBook.status == 'active') \
            .join(Book) \
            .all()
    else:
        recent_posts = []
        active_books = []

    return render_template("home.html", recent_posts=recent_posts, active_books=active_books)

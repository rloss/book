from app import db
from datetime import datetime

class Post(db.Model):
    __tablename__ = "posts"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"), nullable=True)
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text, nullable=False)
    visibility = db.Column(db.String(20), default="public")  # 'public', 'group', 'private'
    scope = db.Column(db.String(20), default="personal")     # 'personal', 'common'
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 관계 정의 (선택적)
    user = db.relationship("User", backref="posts")
    book = db.relationship("Book", backref="posts")

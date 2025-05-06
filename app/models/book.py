from app import db

class Book(db.Model):
    __tablename__ = "books"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    author = db.Column(db.String(100))
    isbn = db.Column(db.String(50), unique=True)
    description = db.Column(db.Text)

    posts = db.relationship("Post", backref="book", lazy=True)

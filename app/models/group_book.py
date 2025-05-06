from app import db

class GroupBook(db.Model):
    __tablename__ = "group_books"

    id = db.Column(db.Integer, primary_key=True)
    group_id = db.Column(db.Integer, db.ForeignKey("groups.id"))
    book_id = db.Column(db.Integer, db.ForeignKey("books.id"))
    status = db.Column(db.String(20), default="active")  # or 'archived'

    book = db.relationship("Book", lazy=True)

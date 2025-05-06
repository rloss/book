from app import db

class Group(db.Model):
    __tablename__ = "groups"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)

    memberships = db.relationship("Membership", backref="group", lazy=True)
    group_books = db.relationship("GroupBook", backref="group", lazy=True)

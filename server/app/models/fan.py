from app import db


class Fan(db.Model):
    __tablename__ = 'fans'
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.Integer)
    state = db.Column(db.Integer, default=1)
    spin = db.Column(db.Boolean, default=False)
    newdata = db.Column(db.Boolean, default=False)

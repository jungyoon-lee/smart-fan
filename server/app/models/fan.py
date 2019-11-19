from app import db


class Fan(db.Model):
    __tablename__ = 'fans'
    id = db.Column(db.Integer, primary_key=True)
    mode = db.Column(db.Integer)                   # 일반모드: 1, 센서모드: 2, 카메라모드: 3
    state = db.Column(db.Integer, default=0)       # 정지: 0, 약풍: 1, 중풍: 2, 강풍: 3
    spin_speed = db.Column(db.Integer, default=0)  # 안회전: 0, 회전: 1

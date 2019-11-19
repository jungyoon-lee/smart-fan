from flask import Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy

from config import CONNECT_STRING

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = CONNECT_STRING
app.config['SECRET_KEY'] = 'super secret key'
app.config['SESSION_TYPE'] = 'filesystem'

db = SQLAlchemy(app)

from app import models
db.create_all()

from app import routes

from app.models.fan import Fan

def init_create_db():
    fan = Fan.query.filter_by(id=1).first()

    if fan is None:
        fan = Fan(mode=1, state=False, newdata=False)
        print(fan)
        db.session.add(fan)
        db.session.commit()

@app.route('/')
def index():
    fan = Fan.query.filter_by(id=1).first()

    if fan is None:
        init_create_db()
        return render_template('index.html')

    if fan.mode is 1:
        return redirect(url_for('normal'))
    elif fan.mode is 2:
        return redirect(url_for('sensor'))
    elif fan.mode is 3:
        return redirect(url_for('face'))

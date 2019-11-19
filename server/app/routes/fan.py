from flask import render_template, request, url_for, flash, jsonify, redirect, abort
import time

# from app.models.fan import Fan
from app import app, db
from app.models.fan import Fan

def choose_mode(mode):
    fan = Fan.query.filter_by(id=1).one()
    fan.mode = mode

    db.session.add(fan)
    db.session.commit()


# fan.speed()
# head_spin(left, right, speed)

# 노말 모드 1
@app.route('/normal', methods=["GET", "POST"])
def normal():
    choose_mode(1)


    return render_template('fan/normal.html')


# 센서 인식모드 2
@app.route('/sensor', methods=["GET", "POST"])
def sensor():
    choose_mode(2)



    return render_template('fan/sensor.html')


# 얼굴인식 모드 3
@app.route('/face', methods=["GET", "POST"])
def face():
    choose_mode(3)


    return render_template('fan/face.html')

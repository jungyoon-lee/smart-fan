from flask import render_template, request, url_for, flash, jsonify, redirect, abort
import time

# from app.models.fan import Fan
from app import app, db
from app.models.fan import Fan
#from motor import fan_speed, head_spin
#from sensor import measure

slow = 50
middle = 70
strong = 100

# fan.speed()
# head_spin(left, right, speed)
def choose_mode(mode):
    fan = Fan.query.filter_by(id=1).one()
    fan.mode = mode

    db.session.add(fan)
    db.session.commit()


@app.route('/wind/<int:value>', methods=["POST"])
def wind_1(value):
    # fan_speed(value)
    print(value)
    fan = Fan.query.filter_by(id=1).one()
    fan.state = value
    db.session.add(fan)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/spin', methods=["POST"])
def spin():
    # head_spin(10)

    fan = Fan.query.filter_by(id=1).one()

    if fan.spin_speed is 0:
        fan.spin_speed = 10
    else:
        fan.spin_speed = 0

    db.session.add(fan)
    db.session.commit()

    return redirect(url_for('index'))


@app.route('/timer', methods=["POST"])
def timer():
    time = request.form['time']
    fan = Fan.query.filter_by(id=1).one()

    current_time = time.time()


    if current_time+1000:
        fan.speed = 0


    return redirect(url_for('index'))


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

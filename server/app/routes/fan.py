from flask import render_template, request, url_for, flash, jsonify, redirect, abort, Response
import time
import threading

from app import app, db
from app.models.fan import Fan
import face_recog

#from motor import fan_speed, head_spin
#from sensor import sensing

slow = 50
middle = 70
strong = 100

# fan.speed()
# head_spin(left, right, speed)
def choose_mode(mode):
    fan = Fan.query.filter_by(id=1).one()

    fan.mode = mode
    fan.state = 0
    fan.spin_speed = 0

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


@app.route('/sensing', methods=["POST"])
def sensing():
    left, right = sensing()

    fan = db.query.filter_by(id=1).one()

    fan.left = left
    fan.right = right

    db.session.add(fan)
    db.session.commit()

    return render_template('fan/sensor.html')


def gen(file):
    while True:
        jpg_bytes = file.get_jpg_bytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + jpg_bytes + b'\r\n\r\n')


@app.route('/video_feed')
def video_feed():
    return Response(
        gen(face_recog.FaceRecog()),
        mimetype='multipart/x-mixed-replace; boundary=frame'
    )


# 노말 모드 1
@app.route('/normal_mode', methods=["GET", "POST"])
def normal_mode():
    choose_mode(1)


    return render_template('fan/normal.html')


# 센서 인식모드 2
@app.route('/sensor_mode', methods=["GET", "POST"])
def sensor_mode():
    choose_mode(2)


    return render_template('fan/sensor.html')


# 얼굴인식 모드 3
@app.route('/face_mode', methods=["GET", "POST"])
def face_mode():
    choose_mode(3)


    return render_template('fan/face.html')




from flask import render_template, request, url_for, flash, jsonify, redirect, abort, Response
import time
import requests
import RPi.GPIO as GPIO

from app import app, db
from app.models.fan import Fan

from app.routes.dc_motor import dc_motor
slow = 50
middle = 70
strong = 100

GPIO.setmode(GPIO.BCM)
SW1 = 18
SW2 = 23
SW3 = 24
SW4 = 25
SW5 = 12

GPIO.setup(SW1,GPIO.IN)
GPIO.setup(SW2,GPIO.IN)
GPIO.setup(SW3,GPIO.IN)
GPIO.setup(SW4,GPIO.IN)
GPIO.setup(SW5,GPIO.IN)


def choose_mode(mode):
    fan = Fan.query.filter_by(id=1).one()

    fan.mode = mode
    fan.state = 0
    fan.spin_speed = 0

    db.session.add(fan)
    db.session.commit()


@app.route('/sensor/handshake', methods=["GET", "POST"])
def sensor_handshake():
    url = 'http://172.20.10.12:8080/sensing'
    res = requests.get(url)
    
    return redirect(url_for('index'))


@app.route('/sensor/enroll', methods=["GET", "POST"])
def sensor_enroll():
    if request.method == "POST":
        url = 'http://172.20.10.12:8080'
        data = request.form
        print(data['left'])
        print(data['right'])
 
        fan = Fan.query.filter_by(id=1).one()
        fan.left = int(data['left']) * 30
        fan.right = int(data['right']) * 30
        
        print(fan.left)
        print(fan.right)

        db.session.add(fan)
        db.session.commit()

    return '이정윤 천재'


@app.route('/timer', methods=["POST"])
def timer():
    time = request.form['time']
    fan = Fan.query.filter_by(id=1).one()

    current_time = time.time()

    if current_time+1000:
        fan.speed = 0

    return redirect(url_for('index'))


def reset_spin():
    fan = Fan.query.filter_by(id=1).one()
   
    fan.left = 0
    fan.right = 180
    
    db.session.add(fan)
    db.session.commit()

    return 'hello'


# 노말 모드 1
@app.route('/normal_mode', methods=["GET", "POST"])
def normal_mode():
    choose_mode(1)
    reset_spin()
    
    key_1 = GPIO.input(SW1)
    key_2 = GPIO.input(SW2) #week
    key_3 = GPIO.input(SW3) #mid
    key_4 = GPIO.input(SW4) #strong
    key_5 = GPIO.input(SW5) #stop

    if key_2 == 1:
        dc_motor(50)
    elif key_3 == 1:
        dc_motor(30)
    elif key_4 == 1: 
        dc_motor(5)
    elif key_5 == 1:
        dc_motor(100)

    return render_template('fan/normal.html')


# 센서 인식모드 2
@app.route('/sensor_mode', methods=["GET", "POST"])
def sensor_mode():
    choose_mode(2)
   
    key_1 = GPIO.input(SW1)
    key_2 = GPIO.input(SW2) #week
    key_3 = GPIO.input(SW3) #mid
    key_4 = GPIO.input(SW4) #strong
    key_5 = GPIO.input(SW5) #stop

    if key_2 == 1:
        dc_motor(50)
    elif key_3 == 1:
        dc_motor(30)
    elif key_4 == 1: 
        dc_motor(5)
    elif key_5 == 1:
        dc_motor(100)

    return render_template('fan/sensor.html')


# 얼굴인식 모드 3
@app.route('/face_mode', methods=["GET", "POST"])
def face_mode():
    choose_mode(3)

    return render_template('fan/face.html')

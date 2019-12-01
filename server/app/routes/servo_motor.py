import RPi.GPIO as GPIO
import time
from flask import Flask, redirect, url_for

from app import app, db
from app.routes.fan import Fan
SRV = 17
freq = 100.0

GPIO.setmode(GPIO.BCM)
GPIO.setup(SRV, GPIO.OUT, initial = GPIO.LOW)
p = GPIO.PWM(SRV, freq)

def convert_dc(deg):
    deg_min = 0.0
    deg_max = 180.0
    dc_min = 5.0
    dc_max = 22.0
    
    return ((deg - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)


@app.route('/spin', methods=["GET", "POST"])
def servo(): #basis speed = 1 and time.sleep = 0.02 speed should < r-l
    fan = Fan.query.filter_by(id=1).one()
    left = fan.left
    right = fan.right
    speed = 1

    if speed >= right - left:
        return 0
    
    right += 25  

    if(speed == 1):
        tm = speed * 0.05
    else:
        tm = speed * 0.02

    p.start(0)

    try:
        while 1:
            for deg in range(left, right + 1, speed):
                dc = convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                time.sleep(tm)
                
            for deg in range(right, left - 1, -speed):
                dc = convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                time.sleep(tm)                    

    except:
        p.stop()

    return redirect(url_for('index'))


@app.route('/spin/stop', methods=["GET", "POST"])
def servo_stop():
    fan = Fan.query.filter_by(id=1).one()

    f = open("app/routes/fan.py", mode='at')

    f.writelines(['print()', '\n'])
    f.close()

    return redirect(url_for('index'))

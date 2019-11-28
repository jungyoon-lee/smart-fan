from app import app
import RPi.GPIO as GPIO
from flask import request
import time

# high = 0
# mid  = 20
# low  = 50
# stop = 0

GPIO.setmode(GPIO.BCM)

AIN1 = 13
PWMA = 19

GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

p_dc = GPIO.PWM(PWMA, 100)

p_dc.start(0)

@app.route('/wind/<int:speed>', methods=["GET", "POST"])
def dc_motor(speed): #0 <= speed <= 100
    if request.method == "POST":

        if speed == 100:
            GPIO.output(AIN1, GPIO.LOW)
        else:
            GPIO.output(AIN1, GPIO.HIGH)
            p_dc.ChangeDutyCycle(speed)

    return (''), 204

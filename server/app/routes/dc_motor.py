from app import app
import RPi.GPIO as GPIO
from flask import request, redirect, url_for
import time

# high = 0
# mid  = 20
# low  = 50
# stop = 0


#p_dc.ChangeDutyCycle(100)
GPIO.setmode(GPIO.BCM)
AIN1 = 13
PWMA = 19

GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

p_dc = GPIO.PWM(PWMA, 100)

p_dc.start(0)


@app.route('/wind/<int:speed>', methods=["GET", "POST"])
def dc_motor(speed): #0 <= speed <= 100
    if speed == 100:
        GPIO.setmode(GPIO.BCM)

        GPIO.setup(AIN1, GPIO.OUT, initial=GPIO.LOW)
        GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)

        p_dc.start(0)

    else:
        GPIO.output(AIN1, GPIO.HIGH)
        p_dc.ChangeDutyCycle(speed)
         
    return redirect(url_for('index'))

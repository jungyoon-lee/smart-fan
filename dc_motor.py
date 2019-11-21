import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

SW = 25
AIN1 = 13
PWMA = 19

GPIO.setup(AIN1, GPIO.OUT, initial = GPIO.LOW)
GPIO.setup(PWMA, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(SW,GPIO.IN)

p=GPIO.PWM(PWMA,100)

p.start(0)

try:
    while 1:
        key_in = GPIO.input(SW)
        if key_in == 1:
            while 1:
                GPIO.output(AIN1, GPIO.HIGH)
                p.ChangeDutyCycle(20)
        else:
            print("xzll")
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleanup()

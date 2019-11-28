import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO,BCM)

SW=18
SRV=17

GPIO.setup(SW,GPIO.IN)
GPIO.setup(SRV,GPIO.OUT)

freq = 100.0
deg_min = 0.0
deg_max = 180.0
dc_min=5.0
dc_max = 22.0

def convert_dc(deg):
    return ((deg-deg_min)*(dc_max-dc_min)/(deg_max-deg_min)+dc_min)

p=GPIO.PWM(SRV,freq)

p.start(0)

try:
    while 1:
        key_in=GPIO.input(SW)
        if key_in == 1:
            for deg in range(0,181,180):
                dc = convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                time.sleep(0.5)
            for deg in range(180,-1,-180):
                dc = convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                time.sleep(0.5)
        else:
            print("sd")
except KeyboardInterrupt:
    pass

p.stop()
GPIO.cleenup()
            
            

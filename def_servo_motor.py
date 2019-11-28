import RPi.GPIO as GPIO
import time

def convert_dc(deg):
    deg_min = 0.0
    deg_max = 180.0
    dc_min = 5.0
    dc_max = 22.0
    
    return ((deg - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)


def servo(l,r,speed): #basis speed = 1 and time.sleep = 0.02 speed should < r-l
    if speed >= r-l:
        return 0
    
    GPIO.setmode(GPIO.BCM)

    SRV = 17
    r+=25
    
    GPIO.setup(SRV,GPIO.OUT)

    freq = 100.0
    tm = speed*0.02
    
    p = GPIO.PWM(SRV, freq)
    p.start(0)

    try:
        while 1:
            for deg in range(l, r+1, speed):
                dc = convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                time.sleep(tm)
                
            for deg in range(r, l-1, -speed):
                dc = convert_dc(float(deg))
                p.ChangeDutyCycle(dc)
                time.sleep(tm)                    
                                    
    except KeyboardInterrupt:
        pass
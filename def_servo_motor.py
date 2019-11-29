import RPi.GPIO as GPIO
import time
from flask import Flask

app = Flask(__name__)

SRV = 17
freq = 100.0
GPIO.setmode(GPIO.BCM)
GPIO.setup(SRV, GPIO.OUT)
p = GPIO.PWM(SRV, freq)

def convert_dc(deg):
    deg_min = 0.0
    deg_max = 180.0
    dc_min = 5.0
    dc_max = 22.0
    
    return ((deg - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)


@app.route('/spin')
def servo(l = 0, r = 180, speed = 1): #basis speed = 1 and time.sleep = 0.02 speed should < r-l
    if speed >= r-l:
        return 0
    
    r += 25  

    if(speed==1):
        tm = speed*0.05
    else:
        tm = speed*0.02
   
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
    except:
        pass

                                    

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

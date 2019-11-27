import RPi.GPIO as GPIO
import time


def dc_motor(speed): #0<speed<=100
    while 1:
        GPIO.setmode(GPIO.BCM)   
        
        AIN1 = 13
        PWMA = 19
        
        GPIO.setup(AIN1, GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(PWMA, GPIO.OUT,initial=GPIO.LOW)
        
        p_dc=GPIO.PWM(PWMA,100)

        p_dc.start(0)
        
        print(speed)
        
        
        while 1:
            GPIO.output(AIN1,GPIO.HIGH)
            p_dc.ChangeDutyCycle(speed)
            
            
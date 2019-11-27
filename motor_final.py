import RPi.GPIO as GPIO
import time

def motor(l,r):
    while 1:
        GPIO.setmode(GPIO.BCM)

        SW1 = 18
        SW2 = 23
        SW3 = 24
        SW4 = 25
        SW5 = 12
        SRV = 17
        
        AIN1 = 13
        PWMA = 19
        
        freq = 100.0
        deg_min = 0.0
        deg_max = 180.0
        dc_min = 5.0
        dc_max = 22.0

        x=r-l
        k1=(0.65*x)/200
        k2=(0.45*x)/200
        
        def convert_dc(deg):
                return ((deg - deg_min) * (dc_max - dc_min) / (deg_max - deg_min) + dc_min)

        

        GPIO.setup(AIN1, GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(PWMA, GPIO.OUT,initial=GPIO.LOW)
        GPIO.setup(SRV,GPIO.OUT)
        GPIO.setup(SW1,GPIO.IN)
        GPIO.setup(SW2,GPIO.IN)
        GPIO.setup(SW3,GPIO.IN)
        GPIO.setup(SW4,GPIO.IN)
        GPIO.setup(SW5,GPIO.IN)
        
        p_servo = GPIO.PWM(SRV, freq)
        p_dc=GPIO.PWM(PWMA,100)

        p_dc.start(0)
        p_servo.start(0)
        

        try:
            while 1:
                key_1 = GPIO.input(SW1)
                key_2 = GPIO.input(SW2) #week
                key_3 = GPIO.input(SW3) #mid
                key_4 = GPIO.input(SW4) #strong
                key_5 = GPIO.input(SW5) #stop
                if key_1 == 1:
                    while 1:
                        key_1 = GPIO.input(SW1)
                        key_2 = GPIO.input(SW2) 
                        key_3 = GPIO.input(SW3) 
                        key_4 = GPIO.input(SW4) 
                        key_5 = GPIO.input(SW5)
                        for deg in range(l, r+1, x):
                            dc = convert_dc(float(deg))
                            p_servo.ChangeDutyCycle(dc)
                            time.sleep(k1)
                        for deg in range(r, l-1, -x):
                            dc = convert_dc(float(deg))
                            p_servo.ChangeDutyCycle(dc)
                            time.sleep(k2)
                        if key_5 == 1 or key_4 == 1 or key_3 == 1 or key_2 == 1:
                            break
                elif key_2 == 1:
                    while 1:
                        key_1 = GPIO.input(SW1)
                        key_2 = GPIO.input(SW2) 
                        key_3 = GPIO.input(SW3) 
                        key_4 = GPIO.input(SW4) 
                        key_5 = GPIO.input(SW5)               
                        GPIO.output(AIN1,GPIO.HIGH)
                        p_dc.ChangeDutyCycle(20)
                        if key_5 == 1 or key_4 == 1 or key_3 == 1 or key_1 == 1: 
                            break
                elif key_3 == 1:
                    while 1:
                        key_1 = GPIO.input(SW1)
                        key_2 = GPIO.input(SW2) 
                        key_3 = GPIO.input(SW3) 
                        key_4 = GPIO.input(SW4) 
                        key_5 = GPIO.input(SW5)              
                        GPIO.output(AIN1,GPIO.HIGH)
                        p_dc.ChangeDutyCycle(10)
                        if key_5 == 1 or key_4 == 1 or key_2 == 1 or key_1 == 1:
                            break
                elif key_4 == 1:
                    while 1:
                        key_1 = GPIO.input(SW1)
                        key_2 = GPIO.input(SW2) 
                        key_3 = GPIO.input(SW3) 
                        key_4 = GPIO.input(SW4) 
                        key_5 = GPIO.input(SW5)              
                        GPIO.output(AIN1,GPIO.HIGH)
                        p_dc.ChangeDutyCycle(5)
                        if key_5 == 1 or key_3 == 1 or key_2 == 1 or key_1 == 1:
                            break
                elif key_5 == 1:
                    while 1:
                        key_1 = GPIO.input(SW1)
                        key_2 = GPIO.input(SW2) 
                        key_3 = GPIO.input(SW3) 
                        key_4 = GPIO.input(SW4) 
                        key_5 = GPIO.input(SW5)              
                        GPIO.output(AIN1,GPIO.HIGH)
                        p_dc.ChangeDutyCycle(100)
                        p_servo.ChangeDutyCycle(100)
                        if key_4 == 1 or key_3 == 1 or key_2 == 1 or key_1 == 1:
                            break        
        except KeyboardInterrupt:
            pass

    p.stop()
    GPIO.cleanup()

motor(30,150)
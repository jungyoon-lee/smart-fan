import RPi.GPIO as gpio
import time

def observation(trig,echo):
    gpio.output(trig,False)
    time.sleep(0.5)
    gpio.output(trig,True)
    time.sleep(0.00001)
    gpio.output(trig,False)
    
    while gpio.input(echo) == 0:
        pulse_start=time.time()
        
    while gpio.input(echo) == 1:
        pulse_end=time.time()
        
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration*17000
    distance = round(distance,2)
    
    return distance


def range_check(sensors, human_location):            
    for i in range(7):
        if sensors[i] != 0:
            human_location[i] = 1
    
    return human_location
        
    
def find_left(li):
    for i in range(7):
        if li[i] == 1:
            return i
    return 0

        
def find_right(li):
    for i in range(6,-1,-1):
        if li[i] == 1:
            return i
    return 0


def sensing():
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    
    left = 0
    right = 0
    trig = [5, 20, 23, 17, 26, 12, 4]
    echo = [6, 21, 24, 18, 27, 13, 22]
    human_location=[0, 0, 0, 0, 0, 0, 0]
    sensors=[0, 0, 0, 0, 0, 0, 0]
    
    for i in range(7):
        gpio.setup(trig[i], gpio.OUT)
        gpio.setup(echo[i], gpio.IN)

        sensor[i] = observation(trig[i],echo[i])

        if sensor[i]>70:
            sensor[i]=0
  
    print(fir)
    print(sec)
    print(thd)
    print(fot)
    print(fit)
    print(sit)
    print(sev)
    
    human_location = range_check(sensors, human_location)
    
    left = find_left(human_location)
    right = find_right(human_location)
    
    return left,right


left, right = sensing()
print(left)
print(right)

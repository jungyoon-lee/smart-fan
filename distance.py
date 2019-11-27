import RPi.GPIO as gpio
import time

def sensing(turn):
    gpio.setmode(gpio.BCM)
    gpio.setwarnings(False)
    trig1=5
    echo1=6

    trig2=20
    echo2=21

    trig3=23
    echo3=24

    trig4=17
    echo4=18

    trig5=26
    echo5=27

    trig6=12
    echo6=13

    trig7=4
    echo7=22
    #센서를 추가할 것이면 trig2=16 echo2=20 처럼 선 꼽는 위치 쓰고 33 while문에 함수 호출 추가하면 끝!
    gpio.setup(trig1,gpio.OUT)
    gpio.setup(trig2,gpio.OUT)
    gpio.setup(trig3,gpio.OUT)
    gpio.setup(trig4,gpio.OUT)
    gpio.setup(trig5,gpio.OUT)
    gpio.setup(trig6,gpio.OUT)
    gpio.setup(trig7,gpio.OUT)

    gpio.setup(echo1, gpio.IN)
    gpio.setup(echo2, gpio.IN)
    gpio.setup(echo3, gpio.IN)
    gpio.setup(echo4, gpio.IN)
    gpio.setup(echo5, gpio.IN)
    gpio.setup(echo6, gpio.IN)
    gpio.setup(echo7, gpio.IN)


def observation(trig,echo):
    gpio.output(trig,False)
    time.sleep(0.5)
    gpio.output(trig,True)
    time.sleep(0.00001)
    gpio.output(trig,False)
    
    while gpio.input(echo)==0:
        pulse_start=time.time()
        
    while gpio.input(echo)==1:
        pulse_end=time.time()
        
    pulse_duration=pulse_end - pulse_start
    distance=pulse_duration*17000
    distance=round(distance,2)
    
    return distance


def range_check(sensors,human_location):
    i=0
    while i<8: #센서 수에 따라 변경
        if i==7: #센서 수에 따라 변경
            return sensors,human_location
        elif sensors[i]!=0:
            human_location[i]=1
            i+=1
        else:
            i+=1

human_location=[0,0,0,0,0,0,0]

    
def find_left(li):
    for i in range(7):
        if li[i]==1:
            return i
        
        
def find_right(li):
    for i in range(6,-1,-1):
        if li[i]==1:
            return i
    
    while turn:
        danger=0
        sensors=[0,0,0,0,0,0,0]

        fir=observation(trig1,echo1)
        sec=observation(trig2,echo2)
        thd=observation(trig3,echo3)
        fot=observation(trig4,echo4)
        fit=observation(trig5,echo5)
        sit=observation(trig6,echo6)
        sev=observation(trig7,echo7)
        #sensors라는 빈 리스트에 각각 센서들의 거리값을 저장
        if fir<=50 and sec<=50 and thd<=50 and fot<=50 and fit<=50 and sit<=50 and sev<=50: #센싱한 거리에 따른 실행 조건문
            sensors[0]=fir
            sensors[1]=sec
            sensors[2]=thd
            sensors[3]=fot
            sensors[4]=fit
            sensors[5]=sit
            sensors[6]=sev
            
            sensors,human_location=range_check(sensors,human_location)
            
            left=find_left(human_location)
            right=find_right(human_location)
            
            return left,right

        elif fir>=3 and sec>=3 and thd>=3 and fot>=3 and fit>=3 and sit>=3 and sev>=3:
            danger=1
            #선풍기와 너무 가까운 상황일때 선풍기 멈추는 함수 추가 바람
        else:
            danger=0


        print("distance:",fir,"cm\n","distance2:",sec,"cm")
        


left, right = sensing(1)
print(left)
print(right)
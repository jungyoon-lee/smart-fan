# 센서 서버
하는 일 : 메인 서버가 센서 값을 센서 서버에게 요청하면 센서 서버가 센서 값(left, right)으로 응답함.

#### Python
```buildoutcfg
1. python3, python3-pip을 설치한다.
    $ sudo apt install python3 python3-pip
```

#### Virtualenv
```buildoutcfg
1. virtualenv 설치한다.
    $ sudo apt install virtualenv
    
    (error) 만약 에러가 난다?
        $ sudo apt-get install letsencrypt
        $ export LC_ALL="en_US.UTF-8"
        $ export LC_CTYPE="en_US.UTF-8"

2. 프로젝트에 venv(가상환경)을 만든다.
    $ virtualenv venv -p python3

3. venv을 활성화한다.
    $ source ./venv/bin/activate
```

#### 라이브러리 설치
```buildoutcfg
1. 라이브러리를 설치한다.
     $ pip install -r requirements.txt
```

## 실행편
```buildoutcfg
1. venv을 활성화한다.
     $ source ./venv/bin/activate

2-1. 실행한다.
     $ flask run

포트번호를 바꾸고 싶다.
    - runserver.py에서 바꾼다.
     $ python runserver.py
```

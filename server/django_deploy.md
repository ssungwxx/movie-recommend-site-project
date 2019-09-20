# Django 배포하기

사용 환경 : Django + virtualenv + gunicorn + Nginx + Supervisor

### 왜 gunicorn + Nginx 환경을 세팅하였는가?

Django는 Python언어로 이루어져 있기때문에 웹 서버(Nginx)가 바로 해석할 수 없다. 그렇기에 프로그래밍 언어를 해석할 수 있는 인터페이스, CGI(Common Gateway Interface)가 필요하다.

그 중, WSGI는 python 애플리케이션과 웹 서버가 통신하기 위해 정의된 표준 인터페이스 스펙이다.
CGI와 WSGI는 웹 요청을 처리할 수 있는 표준 인터페이스 프로그램이라는 점에서 같지만, CGI는 WSGI보다 low level에 존재한다.
제사한 내용은 [여기](https://stackoverflow.com/questions/4929626/what-are-wsgi-and-cgi-in-plain-english)를 참고하면된다.

보통 WSGI는 uWSGI를 많이 사용하고 있지만 너무 무겁고 자원을 많이 사용한다는 이슈가 있어서 [gunicorn](https://gunicorn.org)을 사용하였다.
gunicorn은 좀 더 가볍고 빠르게 세팅이 가능하며 속도가 더 빠르다고 한다.

gunicorn은 Nginx와 같이 쓰기를 권장하고 있기에 최종적으로 gunicorn + nginx 환경을 사용하기로 하였다.

참고로, gunicorn의 발음은 지유니콘이다.

### Supervisor란?

Supervisor는 등록된 util을 모니터링하고 죽으면 다시 가동시키는 역활을 하는 python package이다. 잘못된 요청이 들어와서 서버가 죽어버릴 경우를 대비하여 설정하였다.

## 설치 방법

### virtualenv + Django 설정

설치 하기전에 package를 update/upgrade 해준다.

```
sudo apt-get update
sudo apt-get upgrade
```

그 다음로는 python 패키지를 설치하기 위한 pip을 설치한다.
python 버전은 python 3.6.8버전을 사용중이다.

```
sudo apt-get install python3-pip
```

파이썬 가상환경을 위한 virtualenv를 설치한다.

```
sudo pip3 install virtualenv
```

가상환경의 설정파일을 가지고있는 폴더를 생성한다.
폴더 경로는 */home/ubuntu/bigdataProject*로 하였다

```
virtualenv /home/ubuntu/bigdataProject
```

이 이후 작업은 가상환경을 실행하여 작업한다.
작동 코드 :

```
source /home/ubuntu/bigdateProject/bin/activate
```

Django를 실행하기 위한 패키지를 설치한다. REST API를 사용하기 위한 패키지도 같이 설치해준다.

```
pip3 install django
pip3 install djangorestframework
```

Git에서 프로젝트를 clone해온다. 해당 프로젝트의 폴더명은 backend이다.

```
git clone [Git 주소명.git]
```

프로젝트로 이동하고 DB생성을 위한 기본작업을 해준다. DB는 SQLite를 사용하고 있다.

```
cd backend
sudo python3 manage.py migrate
sudo python3 manage.py migrate --run-syncdb
```

이때, *sudo python3 manage.py migrate --run-syncdb*명령어를 사용하지 않으면 데이터를 삽입하는 과정에서 테이블이 없다는 오류가 발생한다. 로컬환경에서는 발생하지 않았던 오류였기에 추후 확인 해야함

정상적으로 작동하는지 확인해본다.

```
sudo python3 manage.py runserver
```

localhost:8000/admin 페이지가 정상적으로 접속이 되는지 확인한다.
해당 명령어는 개발단계에서 쓰이는 명령어이므로, 이 방법으로 웹서버를 배포하면 안된다. 정상적으로 작동하는 것을 확인하였으면 종료한다.

### gunicorn 설정

먼저 gunicorn을 설치한다.

```
sudo pip3 install gunicorn
```

설치하고 작동을 확인한다.

```
gunicorn --bind 0.0.0.0:8030 myproject.wsgi
```

위 명령어를 통해 모든 아이피에 대해 8030포트를 열어주었다.
웹 사이트로 접속하여 확인한다.

아래 명령어를 통해 gunicorn을 Supervisor에 올릴 것이다.
worker의 경우 싱글코어경우 3이 적당하는 글을 읽었는데 출처를 까먹어서 기재 못한다. 다시 찾을경우 계산방법이 있는 출처를 올릴예정

```
gunicorn --daemon --workers 3 --bind unix:/home/ubuntu/backend/backend.sock backend.wsgi
```

### Supervisor + Nginx 설정

먼저 supervisor를 설치해준다.

```
sudo apt-get install supervisor
```

그리고 다시 시작해준다.

```
sudo service supervisor restart
```

먼저 시작하기전에 _/etc/supervisor/supervisord.conf_ 에 있는 설정내용을 살펴보자.

```
[include]
files = /etc/supervisor/conf.d/*.conf
```

해당 폴더에 있는 conf확장자를 가진 파일들을 셋팅에 포함한다.
그럼 이제, *backend.conf*파일을 */etc/supervisor/conf.d*에 생성해준다.

```
sudo vi /etc/supervisor/conf.d/backend.conf
```

내용은,

```
[program:backend]
command=/home/ubuntu/bigdataProject/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/backend/backend.sock backend.wsgi
directory=/home/ubuntu/backend
autostart=true
autorestart=true
stderr_logfile=/var/log/backend.err.log
stdout_logfile=/var/log/backend.out.log
```

옵션 설정을 살펴보자면

> command=/home/ubuntu/bigdataProject/bin/gunicorn --workers 3 --bind

이 명령어를 실행한다.

> directory=/home/ubuntu/backend

해당 폴더에서 실행한다.

```
autostart=true
autorestart=true
```

이 명령어로 자동실행 / 자동 재실행이 되도록 한다.

```
stderr_logfile=/var/log/backend.err.log
stdout_logfile=/var/log/backend.out.log
```

이 명령어로 log파일을 남긴다.

아래 명령어로 프로그램을 등록하고 업데이트한다.

```
sudo supervisorctl reread
sudo supervisorctl update
```

아래 명령어로 gunicorn이 실행되는것을 확인할 수 있다.

```
ps ax | grep gunicorn
```

아래 명령어로 상태를 확인할 수 있다.

```
sudo supervisorctl status backend
```

아래 명령어를 통해 파일 변경점을 적용시킨다.

```
sudo supervisorctl reload
```

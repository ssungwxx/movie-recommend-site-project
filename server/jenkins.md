# Jenkins 를 사용하여 자동 배포하기

### 설치 방법

```
sudo apt-get install openjdk-8-jre-headless -y
wget -q -O - https://pkg.jenkins.io/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
```

### Slack 연동

1. Slack App에서 Jenkins CI 설치
2. Connect를 누른 후 메세지가 전송될 채널 선택
3. ID와 Token을 저장
4. Jekins에서 Slack notifications 플러그인 설치
5. 설치 후 Jenkins 관리 -> 시스템 설정 -> Slack으로 이동
6. Workspace에 저장한 ID입력
7. Credential에서 secret text에 토큰을 저장
8. Credential에 저장한 토큰 사용 후 저장
9. Test Connection 버튼을 눌렀을 때 Success문구가 뜨면 성공

### Gitlab Trigger설정

1. Gitlab 플러그인 설치
2. 프로젝트 생성 후 빌드 유발 설정으로 이동
3. Gitlab URL 복사 후 저장
4. 고급 버튼을 눌러 Secret Token 에서 Generate 버튼 클릭 후 token 복사 후 저장
5. Gitlab Integrations로 이동하여 URL과 Token 붙여넣기 후 빌드 유발을 설정할 체크박스 클릭
6. Push Event로 설정하고 브런치 이름을 적으면 특정 브런치 푸쉬 이벤트 발생시 실행 됨
7. 저장 후 테스트 버튼으로 Push Event 클릭 시 Jenkins 프로젝트가 작동하면 성공

## Unit Test 준비

### 시작전에 설치해야할 것들

```
pytest==5.1.3
pytest-django==3.5.1
pep8==1.7.1
pyflakes==2.1.1
pylint==2.3.1
pylint-django==2.0.11
coverage==4.5.4
```

를 requirements.txt에 추가

### Jenkins Shell Script

```
# 백엔드로 이동 & 가상환경 파이썬 작업
cd backend
. /home/ubuntu/bigdataProject/bin/activate
sudo pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate

# 기존 로그 파일 삭제
rm -f results/pep8.log results/pyflakes.log results/coverage.xml

# 유닛테스트 실행 - result.xml 생성
pytest --junitxml=results/result_pytest.xml

# coverage 테스트 - test_sample로 실행
coverage run tests/test_sample.py
coverage xml -o results/coverage.xml
coverage html -d coverage

# pep8, pyflakes log파일 생성
pep8 --config=pep8.cfg uit > results/pep8.log || true
pyflakes test_project > results/pyflakes.log || true

# 배포하기위한 폴더로 복사
sudo cp -Rf ../backend /home/ubuntu/develope
sudo cp -Rf ../data /home/ubuntu/develope

# 현재 위치 변경
cd /home/ubuntu/develope/backend

# 저장해놓은 DB 이동
cp /home/ubuntu/db.sqlite3 ./

# 배포를 위한 재시작
sudo service nginx restart
sudo supervisorctl reload

# 가상환경 종료
deactivate
```

### 참고사이트

https://zetawiki.com/wiki/%EC%9A%B0%EB%B6%84%ED%88%AC_Jenkins_%EC%84%A4%EC%B9%98

https://docs.pytest.org/

https://tomining.tistory.com/147

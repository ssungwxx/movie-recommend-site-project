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

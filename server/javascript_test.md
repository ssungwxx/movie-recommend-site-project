# Vue + Karma + Jasmine

## Karma란?

테스트를 실행시킬 테스트 러너
Angular팀이 제작한 툴

## Jasmine이란?

테스트 코드를 수행할 테스팅 프레임워크

### 왜 Karma + Jasmine 조합인가?

보편적으로 많이 사용되는 테스트 환경을 구축하기위해 선택하였다. 사실 Mocha, Chai, Jest 등 다양한 테스트 툴이 존재하지만 각각의 문제를 해결하는데 집중하기 때문에 상황에 맞춰 조합하여 사용한다. 현재 프로젝트에서는 간단한 테스팅만 수행할 계획이기때문에 이 조합을 선택하였다.

## 설치방법

1. frontend폴더로 이동하여 test를 위한 폴더를 만든다.
2. npm init 명령어로 pakage.json 파일을 제작하는데 이 때, entry point는 js/test.js로 test command는 karma start로 지정한다.
3. Karma, Jasmine, Karma Launcher를 설치한다. 명령어 : npm install karma karma-chrome-launcher jasmine-core --save-dev
4. karma를 실행하기 위해 npm install -g karma-cli 명령어를 통해 설치한다.
5. karma init 명령어를 통해 karma.config.js파일을 생성한다. 이 때, 테스팅할 폴더를 지정하기 위해 위치를 js/\*.js로 js폴더 밑 모든 js파일을 대상으로 지정한다.
6. 테스트를 실핼할 때에는 npm run test를 실행한다.

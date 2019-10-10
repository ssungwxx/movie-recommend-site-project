# Vue를 Nginx를 이용하여 배포

사용 환경 : Vue + Nginx

### Vue Build

Vue cli에서 build를 지원해준다. 옵션으로 webpacke등을 활용하여 빌드를 시도할 수 있다. 현재 프로젝트에서 사용한 옵션은 package.json 파일을 통해 확인할 수 있으며 vue cli를 사용하여 빌드하였다.

```
npm run build
```

명령어를 통해 dist폴더를 생성한다.
해당 폴더는 Vue 프로젝트안에 생성되면 html파일과 js파일을 생성한다.
index.html을 지정하여 빌드하면 된다.

### 문제 사항

Nginx의 기본 옵션으로 배포를 하게되면 메인페이지를 제외한 URL에서 새고침을 할 경우 404 error page가 나타나는 상황이 발생한다.
해당 문제는 Nginx의 url 매핑문제와 현재 프로젝트의 프론트엔드가 SPA로 설계되어있어서 발생한 문제였다.
이 문제는 Nginx의 설정파일에서 URL매핑을 새롭게 해주면 해결된다.

### 참고사이트

[How to handle 404 error request in vuejs SPA with nginx server]](https://stackoverflow.com/questions/52471007/how-to-handle-404-error-request-in-vuejs-spa-with-nginx-server)

# 서울 빅데이터 20조

팀장 : 신승민<br>
팀원 : 김성우, 임성우, 조원철, 지창규<br>
역활분배 : Wiki 참고

## 실행방법

### Backend Server 실행

```
cd backend
python manage.py makemigrations
python manage.py migrate
python manage.py shell < create_admin.txt
python manage.py runserver
```

### Frontend Server 실행

```
cd frontend
npm install
npm install -g yarn
npm install -g @vue/cli
npm install vue
npm runserve
```

### Dataparsing 저장

```
cd data
python parse_data.py
```

### Branch 설명

-   master : 최종 배포 시 업로드
-   release : 릴리즈 파일 배포
-   develope : 개발테스트 후 확인 된 코드 업로드
-   기타 : 각 기능별 테스트 및 작업용

배포 순서 : 기타 브런치 작업 -> develope 브런치로 merge 후 테스트 사이트에서 확인 및 수정 -> release 브랜치에 merge -> 2주 스프린트 완료 후 master 브랜치로 push

### Git 규칙

-   기능 : 기능추가, 삭제, 변경
-   버그 : 버그 수정
-   리팩토링 : 코드 리팩토링
-   형식 : 코드형식, 정렬, 주석 변경
-   테스트 : 테스트 코드 추가, 삭제, 변경
-   문서 : 문서 추가, 삭제, 변경
-   기타 : 기타 사항들

예시

```
"기능 : K-Means 알고리즘 기능 추가"
"버그 : SearchPage 검색 누락 버그 수정"
"문서 : readMe 파일 수정"
```

### Clustering 공부

현재 진행중

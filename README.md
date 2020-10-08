# [Sub PJT 2] 문지기 프로젝트

## Sub PJT 2 란?

- 빅데이터 프로젝트로 데이터 분석을 통한 빅데이터 추천 알고리즘을 구현하여 추천 웹 사이트를 목표로 한다.

### 대표적인 추천 시스템

- 컨텐츠 기반 필터링 (Content Based Filtering: CBF)
  - 추천의 대상이 되는 아이템과 사용자에 대한 이해를 바탕으로 추천하는 방식
- 협업 필터링(Collaborative Filtering: CF)
  - 사용자의 아이템에 대한 기록 정보를 바탕으로 특성 벡터를 직접 수치화하는 것이 아닌 머신러닝 방식으로 자동적으로 수치화함으로써 각 사용자가 무엇을 좋아할지 예측하는 기법



# :smiley: ​프로젝트 소개

### 기획 배경

- 기존 문화재 정책은 문화재 향유 및 문화재 활용 측면에서 부족한 현실
- 국민적 관심 제고를 위해 혁신적인 서비스로 국민의 관심과 참여 유도의 필요성
- 문화재 분야에 과학기술 및 ICT를 통한 새로운 가치 창출

### 프로젝트 이름

![로고](https://user-images.githubusercontent.com/60081201/92375343-f2608e00-f13b-11ea-9644-fcbb36c11497.png)



### 기술 스택

<img src="https://img.shields.io/badge/backend-django-ff69b4" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/frontend-Vue.js-green" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/database-MySQL-yellowgreen" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/server-AWS-9cf" alt="기술스택" style="zoom:120%;" /><img src="https://img.shields.io/badge/language-JavaScript, Python-important" alt="기술스택" style="zoom:120%;" />

![기술스택](https://user-images.githubusercontent.com/60081201/95401187-8befab00-0947-11eb-83ca-bd400f8fff25.PNG)



### :key: ​프로젝트 사용법

로컬 웹 서버 실행 방법은 다음과 같습니다.

#### Frontend

```bash
$ cd frontend/
$ npm install
# 서버를 실행합니다.
$ npm run serve
```

#### Backend

```bash
$ cd backend/
# 가상 환경을 켜줍니다.
$ python -m venv venv
$ source venv/Scripts/activate
# 필요한 설치파일을 다운 받습니다.
$ pip install -r requirements.txt
# 모델링 데이터 베이스에 등록합니다.
$ python manage.py makemigrations
$ python manage.py migrate
# 문화재 데이터를 등록합니다.
$ python manage.py loaddata tag.json
$ python manage.py loaddata heritage_videourl.json
# 서버를 실행합니다.
$ python manage.py runserver
```



### 프로젝트 아키텍처 

- MTV 패턴을 기반으로 한 **django** 백엔드 서버 구축

- MVVM패턴을 기반으로 한 **vue.js** 프론트 엔드 구현



### ERD

<img src="https://user-images.githubusercontent.com/60081201/93542918-3c940b80-f995-11ea-8a27-90a14c5b36f3.png" alt="erd" style="zoom: 33%;" />이거 수정해서 다시올릴기

- 문화재청에서 제공하는 API를 참고하여 작성한 ERD 입니다.



### 와이어 프레임

#### 홈 페이지

- 메인 페이지로 문지기의 기능 소개와 인기 문화재 순위, 월별 행사 정보를 얻을 수 있도록 구성하였습니다.

![메인페이지](https://user-images.githubusercontent.com/60081201/93542917-3c940b80-f995-11ea-9c10-af04445ada53.png)

#### 문화재 추천 페이지

- 문화재 추천 화면에서는 핵심 기능인 사용자 맞춤 문화재 추천 서비스를 제공하며 카로젤로 보여줄 예정입니다.
- 문화재 검색 기능을 갖고 인기 문화재를 무한 스크롤을 이용하여 제공할 것 입니다.

![문화재추천화면](https://user-images.githubusercontent.com/60081201/93542923-3e5dcf00-f995-11ea-935e-d1265904bf34.PNG)

#### 문화재 디테일 페이지

- 문화재 카드를 클릭하게 되면 볼 수 있는 화면으로 관련 문화재에 대한 자세한 정보를 얻을 수 있습니다.
- 위치 정보뿐 아니라 문화재에 대한 리뷰 정보를 볼 수 있도록 구성하였습니다.

![디테일화면](https://user-images.githubusercontent.com/60081201/93542911-3aca4800-f995-11ea-874c-f12c6bb67851.PNG)

#### 게시판 페이지

- 문화재 방문 리뷰를 볼 수 있는 화면으로 인기순과 최신순으로 선택하여 볼 수 있도록 제공할 것입니다.

![게시판](https://user-images.githubusercontent.com/60081201/93543248-0d31ce80-f996-11ea-9535-cfee5b63aa3c.PNG)

#### 지도 페이지

- 카카오맵 API를 활용하여 지도정보를 제공합니다.
- 선택한 지역의 문화재들을 확인할 수 있고 그 주변 시설(편의점, 주유소 등) 정보를 제공합니다.

![지도](https://user-images.githubusercontent.com/60081201/93542935-4158bf80-f995-11ea-9367-5a0e6bd4ddba.PNG)

#### 마이페이지

- 사용자의 찜한 문화재, 리뷰 작성한 게시글 목록을 확인할 수 있는 페이지입니다.
- 사용자의 프로필 설정이 가능하고 리뷰 작성 개수를 기준으로 등급을 주는 재미 요소를 기획하였습니다.
- 성씨를 입력하여 조상님 관련 문화재도 확인할 수 있도록 기획하였습니다.



## 문지기 웹 페이지 기능 소개



## :clipboard: 문화재 추천 `컨텐츠 기반 필터링`

![추천](https://user-images.githubusercontent.com/60081201/95402546-fbb36500-094a-11eb-9366-0a98ad3aff00.PNG)

문화재에 저장되있는 태그의 가중치를 통해 사용자 맞춤 문화재를 추천합니다. 콜드스타트(Cold Start, 데이터가 없는 시작 상태에서는 제대로 동작하지 않는 시스템)를 방지하기 위해 회원가입시에 설문을 받습니다. 이후 사용자가 문화재에 한 좋아요, 찜, 방문체크, 평점 등의 데이터를 통해 정확도 높은 추천 서비스를 제공합니다.

- 평점 : 별점 3을 기준으로 -2에서 2점으로 가중치가 결정합니다.
- 좋아요, 찜 : 1점 가중치를 갖습니다.
- 방문기록 : 추천문화재에서 제거됩니다.



## 기타

### :pushpin: ​Git convention

### Git commit Ground Rule

```bash
$ git commit -m "이슈번호 | 상태 | 작업 설명(optional)"
```

1. 총 70자를 넘지 않는다.
2. 마침표는 사용하지 않는다. 
3. 작업 설명 - 명령문 형식으로 작성 + 현재 시제로 작성

#### 커밋메시지 타입

| git status | 의미                  |
| :--------: | :-------------------- |
|   added    | 추가되었다.           |
|  updated   | 발전되었다.           |
|  deleted   | 삭제되었다.           |
|  replaced  | 대체되었다.           |
|  feature   | 기능 작업 시 사용     |
|    doc     | 문서 작업 시 사용     |
|   style    | 스타일 작업 시 사용   |
|    cicd    | 배포 작업 시 사용     |
|  refactor  | 코드 리팩토링 시 사용 |

#### branch 명명 규칙

|       Branch Name        | 목적                                  |
| :----------------------: | :------------------------------------ |
|          master          | 배포                                  |
|         develop          | Frontend, Backend 각 브랜치 기능 결합 |
| [front/back]/[기능 이름] | 각 기능 개발 브랜치                   |
|         release          | 배포하기 전의 브랜치                  |
|           fix            | 배포버전의 버그 발견시 버그킬 용도    |



### :school: 팀 소개

![esc](https://user-images.githubusercontent.com/60081201/93543792-7108c700-f997-11ea-9642-cb251ae73043.PNG)

#### 나종석 `팀장` `백엔드`

이번 프로젝트에서 팀장을 맡아 1학기부터 알고 지내던 팀원들과 함께 프로젝트를 진행했습니다. 모든 팀원들이 각자 맡은 부분을 성실하게 수행하여 즐겁게 할 수 있었습니다. 이번 특화 프로젝트는 잘 알지 못했던 빅데이터 주제를 처음부터 학습하여 프로젝트를 완성시킬 수 있는 좋은 기회였습니다. 이번 프로젝트를 통해 자신감을 얻고 다음 자율 프로젝트에 임하도록 하겠습니다.

#### 강용준 `백엔드`

이번 프로젝트는 장고와 뷰를 사용해 웹을 작성하고 직접 AWS를 통한 배포를 진행했던 프로젝트였다. 백엔드를 맡아서 진행했으며 DRF를 통한 프론트엔드와의 통신은 이번 프로젝트 중에서 가장 흥미로웠던 부분이였다. 다음 프로젝트에서는 뷰의 동작원리와 백엔드와의 통신에 대해 공부해보고 싶다.

#### 김진혁 `프론트엔드`

지난번 프로젝트는 자바스크립트 본연의 기능에 대해 많이 배웠다면 이번 프로젝트에서는 브라우저와 Vuejs 프레임워크의 기능과 구조에 대해 많이 배웠습니다. Vuejs의 렌더링과 인스턴스, 스케일링과 상태관리에 대해 깊은 이해를 할 수 있었습니다. 다음 프로젝트에서는 자바스크립트를 활용한 백엔드와 프론트엔드 프레임워크에 대해 더 깊게 공부해보고 싶습니다.

#### 최정원 `백엔드`

데이터 APi를 이용해서 정제를 할 때, 미리 사용할 컬럼에 대해서 모두 확정을 지은 뒤, 업무를 수행해야 일을 두번 안해도 됨을 배웠고(실제로 API로 여러번 같은 반복임무를 수행함.) Pandas를 사용해야 빠른 데이터 처리가 가능함을 배웠습니다.

백, 프론트의 몇몇 부분을 구현했는데 매 부분 소통의 중요성을 다시 한 번 배울 수 있었습니다.

#### 신유빈 `프론트엔드`

이번 특화프로젝트를 진행하면서 Vuex를 사용하고 Vue의 장점인 컴포넌트 재사용성을 효율적으로 생각하며 프로젝트를 개발함으로써 보다 성장할 수 있었습니다. 또한 팀원들의 코드리뷰 시간과 지라, 깃랩을 활용하며 팀 프로젝트 진행의 시너지를 많이 느꼈습니다. 또한 이번 빅데이터 특화 프로젝트를 진행하면서 태그 작업을 통해 추천 서비스에 대해 생각해보는 좋은 기회가 되었습니다. 좋은 팀원들을 함께 프로젝트를 하면서 즐겁게 개발할 수 있었습니다.
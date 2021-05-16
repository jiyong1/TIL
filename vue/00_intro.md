# [Vue] Intro

사용자 인터페이스를 만들기 위한 대표적인 프론트엔드 프레임워크 중 하나

- Angular
- React
- Vue.js

<br>

## SPA

> 단일 페이지 어플리케이션 (Single Page Application)

- 현재 페이지를 동적으로 작성함으로써 사용자와 소통하는 웹 어플리케이션
- 단일 페이지로 구성되며 서버로부터 처음에만 페이지를 받아오고 이후에는 `동적으로 DOM을 구성`
- 동작 원리의 일부가 `CSR` 의 구조를 따름

<br>

## CSR

> Client Side Rendering

최초 요청 시 서버로부터 빈 문서를 응답받고 이후 클라이언트에서 데이터를 요청 및 응답받아 DOM을 렌더링하는 방식

- 장점
  - 웹 어플리케이션에 필요한 모든 정적 리소스를 최초에 한번 다운로드 받기 때문에 서버와 클라이언트 간의 트래픽이 감소한다.
  - 전체 페이지를 다시 렌더링하지 않고 변경되는 부분만 갱신하기 때문에 사용자의 경험이 향상된다.
- 단점
  - SEO(검색엔진 최적화) 문제가 발생할 수 있음

<br>

## SSR

> Server Side Rendering

서버측에서 사용자에게 보여줄 페이지를 모두 구성하여 사용자에게 페이지를 보여주는 방식

- 장점
  - 초기 로딩 속도가 빠르기 때문에 사용자가 컨텐츠를 빨리 볼 수 있다.
  - SEO(검색엔진 최적화)가 가능
- 단점
  - 모든 요청에 새롭게 렌더링 되기 때문에 사용자 경험이 떨어진다.
  - 상대적으로 요청 횟수가 많아져 서버 부담이 커진다.

<br>

## MVVM Pattern

> 어플리케이션 로직을 UI로부터 분리하기 위해 설계된 디자인 패턴

- Model : JavaScript Object 자료구조로 Vue Instance 내부에서 data로 사용된다. 값이 바뀌면 View(DOM)가 반응한다.
- View : DOM(HTML)로 data의 변화에 따라서 바뀌는 대상이다.
- View Model: 모든 Vue Instance이다. View와 Model 사이에서 data와 DOM에 관련된 모든 일을 처리한다.

![](00_intro.assets/vuepattern.png)

[이미지 출처: Vue.js 공식문서](https://012.vuejs.org/guide/)
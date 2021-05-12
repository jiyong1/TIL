# [JS] REST API

**REST (REpresentational State Transfer)**는 HTTP를 기반으로 클라이언트가 서버의 리소스에 접근하는 방식을 규정한 방법론이고, **REST API**는 REST를 기반으로 서비스 API를 구현하는 것을 의미한다.

<br>

## 1. REST API의 구성

REST API는 자원, 행위 표현의 3가지 요소로 구성된다. REST API만으로 HTTP 요청의 내용을 이해할 수 있다.

| 구성 요소 | 내용                           | 표현 방법        |
| --------- | ------------------------------ | ---------------- |
| 자원      | 자원                           | URI              |
| 행위      | 자원에 대한 행위               | HTTP 요청 메서드 |
| 표현      | 자원에 대한 해위의 구체적 내용 | 페이로드         |

<br>

## 2. REST API 설계 원칙

REST에서 가장 중요한 기본적인 원칙은 두 가지다.

1. **URI는 리소스를 표현**하는데 집중한다.
   - 리소스를 식별할 수 있는 이름은 동사보다는 명사를 사용한다.
2. 행위에 대한 정의는 HTTP 요청 메서드를 통해 하는 것이다.
   - 클라이언트가 서버에게 요청의 종류와 목적을 알리는 방법이다.
   - **GET, POST, PUT, PATCH, DELETE 등**



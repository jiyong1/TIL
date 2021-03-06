# [WEB] REST API

- **REST** : 분산 하이퍼미디어 시스템(웹)을 위한 아키텍쳐 스타일 (제약조건의 집합)
- **REST API** : REST 아키텍쳐 스타일을 따르는 API

<br>

## 0. 배경

> REST가 생겨나게 된 배경

서버와 클라이언트가 각각 **독립적으로 진화**하기 위해서 REST가 생겨났다. 즉, 서버의 기능이 변경되어도 클라이언트를 업데이트할 필요가 없다는 것이다.

<br>

## 1. REST API의 구성

REST API는 자원, 행위, 표현의 3가지 요소로 구성된다. REST API만으로 HTTP 요청의 내용을 이해할 수 있다.

| 구성 요소 | 내용                           | 표현 방법        |
| --------- | ------------------------------ | ---------------- |
| 자원      | 자원                           | URI              |
| 행위      | 자원에 대한 행위               | HTTP 요청 메서드 |
| 표현      | 자원에 대한 행위의 구체적 내용 | 페이로드         |

<br>

## 2. REST API 설계 원칙

REST에서 가장 중요한 기본적인 원칙은 두 가지다.

- `uniform interface`

1. **URI는 리소스를 표현**하는데 집중한다.
   - 리소스를 식별할 수 있는 이름은 동사보다는 명사를 사용한다.
2. 행위에 대한 정의는 HTTP 요청 메서드를 통해 하는 것이다.
   - 클라이언트가 서버에게 요청의 종류와 목적을 알리는 방법이다.
   - **GET, POST, PUT, PATCH, DELETE 등**
3. Self-descriptive
   - 응답받은 메시지로 메시지가 어떤 의미를 담고 있는지 해석할 수 있어야 한다.
4. HATEOAS (Hypermedia As The Engine Of Application State)
   - 애플리케이션 상태는 Hyperlink를 이용해 전이되어야 한다.

오늘날의 대부분의 REST API라고 하는 것은 **3, 4**번에 대해 잘 지켜지지 않는다. REST는 말 그대로 아키텍처 스타일일뿐 꼭 지켜야하는 규제가 아니기 때문이다. 예를들어 API를 어느 집단내에서만 사용한다면 굳이 **self-descriptive**하지 않아도 된다.

<br>

## 3. 왜 API는 REST가 잘 되지 않는가?

일반적인 웹과 비교해보자.

| 구분         | 웹 페이지 | HTTP API  |
| ------------ | --------- | --------- |
| Protocol     | HTTP      | HTTP      |
| 커뮤니케이션 | 사람-기계 | 기계-기계 |
| Media Type   | HTML      | **JSON**  |

<br>

| 구분             | HTML                                          | JSON               |
| ---------------- | --------------------------------------------- | ------------------ |
| Hyperlink        | a 태그 등을 사용할 수 있다.                   | 정의되어 있지 않음 |
| self-descriptive | HTML 명세를 보면 각 태그의 의미를 알 수 있다. | 불완전하다.        |

- Json은 문법 해석을 통해 파싱이 가능하지만 그 안에 있는 `key`, `value` 값이 무슨 의미를 가지고 있는지 알기 위해서는 별도의 문서가 필요하다.

그렇다면 `Self-descriptive`와 `HATEOAS`가 독립적인 진화에 어떤 도움이 되는가?

- `Self-descriptive`하다면 서버에서 응답의 형태가 변하더라도 그 의미를 해석할 수 있어 독립적인 진화가 가능하다.
- `HATEOAS` : 어디서 어디로의 전이가 미리 결정되지 않고 링크를 응답을 통해 받아올 수 있으므로, **동적으로 링크가 변경될 수 있다.**

<br>

## 4. REST API로 고쳐보자

<br>

### Self-descriptive

- 방법 1
  - media type을 정의한다.
  - media type의 문서를 작성해 IANA에 등록한다.
  - 메세지를 보는 사람은 메세지를 해석할 수 있게 된다.
- 방법 2
  - **profile**을 등록하여 해석하는 명세 링크를 같이 보낸다.

<br>

### HATEOAS

- 방법 1
  - data에 하이퍼링크를 표현한다.
- 방법 2
  - HTTP 헤더에 링크를 추가하여 보낸다.
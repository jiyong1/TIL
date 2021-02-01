# CSS

> Cascading Style sheet



```css
h1 {
    color: blue;
    font-size: 15px;
}
```

- 선택자 : h1
- 선언 :
  - 속성, 값



## 정의 방법

1. 인라인
2. 내부 참조
3. 외부 참조 : head에 rel="stylesheet" href="<링크>"
   - 재사용성을 올리기 위해 외부 참조를 가장 많이 사용한다.



## 선택자

> HTML 문서에서 특정한 요소를 선택하여 스타일링 하기 위해서는 반드시 선택자라는 개념이 필요하다.



- 기본 선택자
  - 전체 선택자(`*`), 요소 선택자
    - h1, h2
  - 클래스 선택자, 아이디 선택자, 속성 선택자
    - id = `#`, class = `.` 
    - class ="name1 name2"  `,`넣지 않는다
- 결합자 (combinarors)
  - 자손 결합자, 자식 결합자
    - 직계 자식 : .`classname` > `직계자식`
  - 일반 형제, 인접 형제 결합자



## class 선택자



- 클래스 선택자는 마침표 문자로 시작하며 해당 클래스가 적용된 문서의 모든 항목을 선택



## id 선택자



- `#` 문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용

- 그러나 id는 문서당 한번만 사용할 수 있으며 요소에는 단일 id 값만 적용 할 수 있다.



## 우선순위



1. 중요도 (!important) - 사용시 주의

2. 우선 순위
   1. 인라인
   2. id 선택자
   3. class 선택자 - 클래스를 많이 사용하자.. 왠만하면
   4. 요소 선택자
   5. 소스 코드 순서



## 상속

> CSS는 상속을 통해 부모 요소의 속성을 자신에게 상속한다.

- 상속 되는 것
  - Text 관련 요소. opacity, visibility 등
- 상속 되지 않는 것 예시
  - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
  - position 관련 요소



## 단위



### 상대 단위

- px
- %
- em
  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐.
- rem
  - 최상위 요소(html)의 사이즈 (16px)를 기준으로 배수를 가짐.
- viewport 기준 단위





## Box model

> 네모네모 세상, 상하좌우



### Margin

- 테두리 바깥의 외부 여백
- shorthand를 통해서 표현이 가능하다.
  - 하나 : 상하좌우
  - 두개 : 상하, 좌우
  - 세개 : 상, 좌우, 하
  - 네개 : 상, 우, 하, 좌 (시계 방향)

### Border

- 테두리 영역
- shorthand 표현 가능

### Padding

- 테두리 안쪽의 내부 여백

### Content

- 글이나 이미지 등 요소의 실제 내용



## display

- display: block ;
  - 줄 바꿈이 일어나는 요소
  - 화면 크기 전체의 가로 폭을 차지한다.
  - 블록 레벨 요소 안에
  - div/ ul, ol, li / p
- diplay: inline
- display: inline-block
- display: none
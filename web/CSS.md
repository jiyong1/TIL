[TOC]

# CSS

> 스타일, 레이아웃 등을 통해 HTML이 사용자에게 어떻게 표시 되는지를 지정하는 언어
>
> 사용자에게 문서(HTML)를 표시하는 방법을 지정하는 언어

<br>

## CSS 구문

- 구문은 선택자와 함께 열린다. 
- 스타일을 지정할 html 요소를 선택. 
- 다음 중괄호가 있는데 이 안에는 속성과 값 쌍 형태를 가지는 하나 또는 그 이상의 선언(declaration)이 있다. 
- 각 쌍은 우리가 선택한 요소의 속성을 지정하고 속성에 부여할 값을 지정한다.

<br>

**선언문** 

- 속성 (Property)
  - 사람이 읽을 수 있는 식별자로, 어떤 (글꼴, 너비, 배경색 등) 스타일 기능을 변경할지 나타냅니다.
- 값 (Value)
  - 각 속성에는 값을 부여한다.
  - 값은 어떻게 (글꼴을 이걸로, 배경 색을 저걸로 등)스타일 기능을 변경할 건지 나타낸다.

<br>

**CSS 정의 방법**

1. `Inline style`
2. 내부 참조 (`Embedding style`)
3. 외부 참조 (`Link style`)

<br>

---

<br>

## CSS Selector

> 선택자는 스타일을 지정할 웹 페이지의 HTML 요소를 대상으로 하는 데 사용

**클래스(class) 선택자**

- 클래스 선택자는 마침표( .) 문자로 시작 하며 해당 클래스가 적용된 문서의 모든 항목을 선택

<br>

**아이디(id) 선택자**

- 아이디 선택자는 `#` 문자로 시작하며 기본적으로 클래스 선택자와 같은 방식으로 사용
- 그러나 아이디는 문서 당 한 번만 사용할 수 있으며 요소에는 단일 id값만 적용 할 수 있다
- 문서에서 동일한 아이디를 여러 번 사용해도 동작하나 그렇게 하면 안된다.

<br>

**결합자**(combinators)

- 자손 결합자
  - 셀렉터A  ` `(공백) 셀렉터B
  - 셀렉터A의 모든 후손 요소(level n) 중 셀렉터B와 일치하는 요소 선택
- 자식 결합자
  - 셀렉터A `>` 셀렉터B
  - 셀렉터A의 모든 자식 요소(level 1) 중 셀렉터B와 일치하는 요소 선택
- 일반 형제 결합자
  - 셀렉터A `~` 셀렉터B
  - 셀렉터A의 형제 요소 중 셀렉터A 뒤에 위치하는 셀렉터B 요소를 모두 선택
- 인접 형제 결합자
  - 셀렉터A `+` 셀렉터B
  - 셀렉터A의 형제 요소 중 셀렉터A 바로 뒤에 위치하는 셀렉터B 요소를 선택
  - 단, A와 B 사이에 다른 요소가 존재하면 선택되지 않음

<br>

**적용 우선순위**

1. `!important`
   - 다른 사람들의 코드에서 발견할 때 그 의미를 알 수 있는 것은 좋다.
   - 하지만 반드시 필요한 경우가 아니면 절대 사용하지 않는 것이 좋다.,
   - `!important` 는 cascading이 정상적으로 작동하는 방식을 변경하므로, CSS 스타일 문제를 해결하기가 어렵습니다.
2. inline style
3. id 선택자
   - id는 대부분의 다른 선택자보다 우선순위가 높기 때문에 다루기가 어려워 질 수 있다.
   - 대부분의 경우 id 보다는 모두  class 선택자로 작성하는 것이 좋다.
   - 만약 문서 내 `링크 이동`이나 `for`를 사용하는 특별한 경우에만 아이디를 사용한다.
4. class 선택자
5. 요소 선택자
6. 소스 순서

<br>

---

<br>

## CSS 단위

**(상대) 크기 단위**

**px**

- 모니터 해상도의 한 화소인 '픽셀'을 기준
- 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

**%**

- 백분율 단위
- 가변적인 레이아웃에서 자주 사용

**em**

- em은 상속의 영향 받음, rem은 최상위 요소(html)를 기준으로 결정됨.
- 상황에 따라 각기 다른 값을 가질 수 있다.

**rem**

- 최상위 요소인 html(root em)을  절대 단위를 기준으로 삼음. 상속의 영향을 받지 않음.
- 상속에 영향을 받지 않기 때문에 대부분의 경우 `rem` 을 많이 사용한다.

**viewport**

- (스크롤을 내리지 않은 상태에서) 웹 페이지를 방문한 유저에게 현재 보이는 웹 컨텐츠의 영역
- viewport를 기준으로한 상대적인 사이즈
- 주로 스마트폰이나 테블릿 디바이스의 화면을 일컫는 용어로 사용된다.
- vw, vh

<br>

**색상 표현 단위**

1. 색상 키워드
   - 색상 키워드는 대소문자를 구분하지 않는 식별자로, red, blue, black처럼 특정 색을 나타낸다
2. RGB 색상
   - 빨강, 초록, 파랑을 통해 특정 색을 표현
   - 16진수 표기법이나 함수형 표기법으로 사용
   - a는 alpha(투명도)가 추가된 것
3. HSL 색상
   - 색상, 채도, 명도를 통해 특정 색상을 표현
   - a는 alpha(투명도)가 추가된 것

<br>

---

<br>

## Box Model

> 웹 디자인은 contents를 담을 box model을 정의하고 CSS 속성을 통해 스타일(배경, 폰트와 텍스트 등)과 위치 및 정렬을 지정하는 것.

- 모든 HTML 요소는 box 형태로 되어있다.
- 하나의 박스는 네 부분(영역)으로 이루어 진다.
  - content / padding / border / margin

<br>

1. Content
   - 글이나 이미지, 비디오 등 요소의 실제 내용
2. Padding (안쪽 여백)
   - Border(테두리) 안쪽의 내부 여백
   - 배경색, 이미지 지정 가능
3. Border
4. Margin (바깥쪽 여백)
   - 테두리 바깥의 외부 여백
   - 배경색 지정 불가

<br>

**마진 상쇄**

- block의 top 및 bottom margin이 때로는 (결합되는 마진 중 크기가) 가장 큰 한 마진으로 결합(combine, 상쇄(collapsed))된다.

<br>

---

<br>

## Display

> display CSS 속성은 요소를 블록과 인라인 요소 중 어느 쪽으로 처리할지와 함께 자식 요소를 배치할 때 사용할 레이아웃을 설정한다.

**block**

- 쌓이는 박스
- 요소는 블록 요소 상자를 생성하여 일반 흐름에서 요소 앞뒤에 줄 바꿈을 생성한다.
- 블록 레벨 요소안에 인라인 레벨 요소가 들어갈 수 있다.

<br>

**inline**

- 줄바꿈이 일어나지 않는 행의 일부 요소
- content 너비만큼 가로 폭을 차지
- width, height, margin-top, margin-bottom을 지정할 수 없음
- 상하 여백은 line-height로 지정

<br>

**inline-block**

- inline 처럼 텍스트 흐름대로 나열, block처럼 박스 형태이기 block 속성 사용가능

<br>

**none**

- 해당 요소를 화면에서 사라지게 하며 요소의 공간조차 사라지게 한다.
- `visibility: hidden;`은 해당 요소를 화면에서 사라지게는 하나 공간은 사라지지 않는다.

<br>

---

<br>

## Position

> CSS Position 요약 

* `position` 속성을 통해 **문서 상에 요소를 배치하는 방법**을 지정한다.

* `top`, `right`, `bottom`, `left` 속성을 통해 **요소의 최종 위치**를 결정한다.

* 사용법은 간단하다.
  1. 기준을 잡는다.  (예- `position: relative;`)
  2. 이동시킨다. (예- `top: 50px;`)



### Position 속성

> 요소를 옮기려면 일단 위치를 옮길 기준점을 잡는다.

| 값       | 의미                             |
| -------- | -------------------------------- |
| static   | 기준 없음 (배치 불가능 / 기본값) |
| relative | 요소 자기 자신을 기준으로 배치   |
| absolute | 부모(조상) 요소를 기준으로 배치  |
| fixed    | 뷰포트 기준으로 배치             |



### Top, Bottom, Left, Right 속성

> 기준점을 잡았으면 다음 네 가지 속성을 이용해서 요소의 위치를 옮길 수 있다.
>
> 요소의 Position 기준에 맞춰 위쪽, 아래쪽, 왼쪽, 오른쪽에서의 거리를 설정한다.

* top : 요소의 position 기준에 맞는 위쪽에서의 거리(위치)를 설정
* bottom : 요소의 position 기준에 맞는 아래쪽에서의 거리(위치)를 설정
* left : 요소의 position 기준에 맞는 왼쪽에서의 거리(위치)를 설정
* right : 요소의 position 기준에 맞는 오른쪽쪽에서의 거리(위치)를 설정



**원본**

```css
<body>
  <div class="grand-parent">
    <div class="parent">
      <div class="child">첫째</div>
      <div class="child relative">둘째</div>
      <div class="child">셋째</div>
    </div>
  </div>
</body>
```

```css
<style>
    .grand-parent {
      width: 500px;
      height: 500px;
      border: 5px dotted lightsalmon;
      padding: 50px;
    }

    .parent {
      width: 500px;
      height: 500px;
      border: 5px dotted lightslategray;
    }

    .child {
      width: 150px;
      height: 100px;
      border: 3px dotted red;
      border-radius: 12px;
      background-color: lightpink;

      display: flex;
      justify-content: center;
      align-items: center;
      font-size: 30px;
    }
</style>
```

![](CSS.assets/cssimg.PNG)



### Relative

> 요소를 일반적인 문서 흐름에 따라 배치한다.
>
> **요소 자기 자신의 원래 위치를 기준으로 배치**한다. (static일때의 position)

- 원래 위치를 기준으로 위쪽(top), 아래쪽(bottom), 왼쪽(left), 오른쪽(right)에서 얼마만큼 떨어질 지 결정한다.
- 위치를 이동하면서 다른 요소에 영향을 주지 않는다.
- 문서 상 원래 위치가 그대로 유지된다.

```css
.relative {
    position: relative;
    left: 100px;
}
```

![](CSS.assets/cssimg2.PNG)



### Absolute

> 요소를 일반적인 문서 흐름에서 제거한다.
>
> **가장 가까운 위치에 있는 조상 요소를 기준으로 배치**한다.

- 조상 요소 위치를 기준으로 위쪽(top), 아래쪽(bottom), 왼쪽(left), 오른쪽(right)에서 얼마만큼 떨어질 지 결정한다.
- 조상 중 Position을 가진 요소가 없다면 초기 컨테이닝 블록를 기준으로 삼는다. (static을 제외한 값)
- 문서 상 원래 위치를 잃어버린다. (아래에 있는 div가 해당 자리를 차지한다)







### 부모 relative & 자식 absolute

> Parent에게 Position 값이 있는 경우?

```css
/* parent absolute */
.parent {
    width: 500px;
    height: 500px;
    border: 5px dotted lightslategray;

    position: relative;
}
.absolute {
    position: absolute;
    /* left: 100px; */
    bottom: 0px;
    right: 0px;
}
```

```css
<div class="grand-parent">
  <div class="parent">
    <div class="child">첫째</div>
    <div class="child absolute">둘째</div>
    <div class="child">셋째</div>
  </div>
</div>
```

![](CSS.assets/cssimg3.PNG)





### 조상 relative & 자식 absolute

> Grandparent에게 Position 값이 있는 경우?

```css
/*grandparent만 relative*/
.grand-parent {
  width: 500px;
  height: 500px;
  border: 5px dotted lightsalmon;
  padding: 50px;

  position: relative;
}

.parent {
  width: 500px;
  height: 500px;
  border: 5px dotted lightslategray;
}
```

![](CSS.assets/cssimg4.PNG)





### 조상 Position 없음 & 자식 absolute

> 부모, 조상 전부 뒤져봐도 Position 값이 없는 경우? (Parent, GrandParent, body태그, html태그까지), **window 객체의 뷰포트를 기준점으로 삼는다.**



---



### Fixed

> viewport를 기준으로
>
> `absolute`를 사용해서 똑같이 구현할 수 있지만, `absolute`는 조상 요소의 위치를 기준점으로 삼는 개념이므로 viewport를 기준점으로 삼으려면 `fixed`를 사용한다.

- 요소를 일반적인 문서 흐름에서 제거한다. 페이지 레이아웃에 어떠한 공간도 배정하지 않는다.
- 뷰포트를 기준점으로 붙어있다 (==화면에 붙어있다.)
  - 쇼핑몰 우측 하단



```css
.absolute {
  position: fixed;
  bottom: 0px;
  right: 0px;
}
```

![](CSS.assets/cssimg5.PNG)





## 참고문헌

https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_Selectors

https://developer.mozilla.org/ko/docs/Learn/CSS/Building_blocks/Cascade_and_inheritance

https://developer.mozilla.org/ko/docs/Web/CSS/inheritance

https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements

https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements

https://developer.mozilla.org/ko/docs/Web/CSS/display

https://docs.emmet.io/cheat-sheet/ 
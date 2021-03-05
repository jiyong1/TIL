# DOM (Document Object Model)

> 객체로 바라본다.



## querySelector

- `document.querySelector('object')` : 맨 앞의 하나를 가져온다.
- `document.querySelectorAll('object')` : 배열과 비슷한 형태로 가져온다.
  - 인덱스 접근으로 하나하나 접근이 가능하다.



## data-

- data-로 시작하는 표준 커스텀 속성
  - data-index, data-id, data-role 등 data-의 형식으로 시작하면 어떤 속성이든 필요에 따라 임의로 추가할 수 있다.

```javascript
const card = document.querySelector('.card')
card.setAttribute('data-id', 123)
```

```html
<div class="card" data-id="123">
    ...
</div>
```



```javascript
const card = document.querySelector('.card')
card.getAttribute('data-id')
```

```
"123"
```



## createElement

> 객체를 만들고 조립하자



- `document.createElement('태그')` : 비어있는 태그 생성
- `비어있는객체.innerHTML` : 태그 내부에 내용 작성
- `부모.appendChild(새로운 친구)` : 부모의 자식 태그로 들어간다.
- `부모.removeChild(자식)` : 지정된 자식  태그를 지운다



## 태그 클래스 수정

- `객체.classList.add('클래스 이름')` 클래스 속성이 추가된다.
- `객체.className = '클래스 이름'` : 클래스 속성을 아예 바꾼다.

- `객체.classList.remove('클래스 이름')` : 클래스 속성 지우기.
- `객체.classList.toggle('클래스 이름')` : 토글 스위치와 비슷하게 클래스 이름을 삭제하거나 추가할 수 있다.
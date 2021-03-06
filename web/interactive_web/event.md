# Event



## Event 함수

- `객체.addEventListenr(type, listner, ?option)`
  - 이벤트 이름, 실행될 함수

```javascript
const ilbunni = document.querySelector('.ilbuni.c');
function clickEventHandler() {
    ilbunni.classList.toggle('special');
}
//
const clickEventHandler = function() {
    ....
}
//
const clickEventHandler = () => {
    ...
}
//
    
ilbunni.addEventListner('click', clickEventHandler);
```



## script 코드 넣기

- html 문서내에 javascript 내용을 추가 할 때 head가 아닌 body태그에 정상적으로 실행된다.

  - 코드는 위에서 아래로 흘러가므로!

  - head에 집어넣으려면 script안에 내용을 추가해야한다.

    ```javascript
    window.addEventListner('load', function(){
        ...
    })
    /* 모든 resource가 로드가 되어야 실행된다. */
    /*---------------------------------------*/
    
    window.addEventListner('DOMContentLoaded', function(){
        ...
    })
    /* 골격구조만 로드가 되면 실행된다. (실행 시점이 더 빠름) */
    ```

  - 귀찮으니까 그냥 body태그에다가 넣자.



### 전역변수 최소화

- 전역변수의 양을 최소화 하자.

  - 협업하는데 다른사람이랑 내 변수의 이름이 충돌할 수 있다.

  - 코드 전체를 함수안에 넣어주자. 그럼 지역변수!

    ```javascript
    (function(){
        const ilbuni = document.querySelector('.ilbuni:nth-child(3)');
        function click(){
            ilbuni.classList.add('special');
        }
        ilbuni.addEventListener('click', click);
    })();
    // 함수 선언과 동시에 바로 실행!
    // 전역변수가 없다.
    ```





## this와 Event 객체



- event 호출 함수의 매개변수에 자동적으로 이벤트 객체가 들어간다.

```javascript
function click(e){
    console.log(e);
}
```

```
MouseEvent {isTrusted: true, screenX: 846, screenY: 197, clientX: 846, clientY: 94, …}
```



- this를 사용하면 이벤트가 발생한 객체를 알 수 있다.

```javascript
function click(){
    console.log(this);
}
```



- `this`와 `이벤트객체.currentTarget`은 querySelector를 통해 얻어낸 객체 전체를 표현하는데 반면, `이벤트객체.target`을 하면 클릭된 자체 객체를 알 수 있다.
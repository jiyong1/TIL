# [JS] 생성자 함수와 객체 생성

> 객체 리터럴은 포함시키지 않았다.

<br>

## object 생성자 함수

```javascript
const person = new Object();

person.name = 'jiyong';
person.greeting = function () {
    console.log('Hi, My name is ' + this.name);
}

person.greeting();
```

- Object 생성자 함수를 호출하면 빈 객체가 생성된다.
- 프로퍼티와 메서드를 추가하여 객체를 완성할 수 있다.
- Object 이외에도 `String, Number, Boolean, Function, Array, Date, RegExp, Promise` 등의 `Built-in` 생성자 함수를 제공한다.

<br>

## 생성자 함수

객체 리터럴에 의해 객체 생성을 하게 되면 동일한 프로퍼티를 가진 객체를 여러개 생성할 때 문제가 발생한다. 따라서 객체를 생성하기 위한 템플릿(Class) 처럼 생성자 함수를 선언한다.

<br>

```javascript
function Person(name) {
    this.name = name;
    this.greeting = function() {
        console.log('Hi, My name is ' + this.name);
    };
}

const jiyong = new Person('jiyong');
const seventwo = new Person('seventwo');
const man = Person('kim'); // 일반 함수로 실행되어 this에 전역 객체가 바인딩 된다.

console.log(name); // kim
```

- new 연산자와 함께 호출하지 않으면 일반 함수로 동작한다.

<br>

함수가 일반 함수로서 호촐되면 함수 객체의 내부 메서드 `[[Call]]` 이 호출되고 new 연산자와 함께 생성자 함수로서 호출되면 내부 메서드 `[[Construct]]` 가 호출된다.

함수 객체는 반드시 callable이어야 한다. 그러나 모든 함수 객체가 [[Construct]]를 갖는 것은 아니다.

<br>

### constructor와 non-constructor

- constructor : 함수 선언문, 함수 표현식, 클래스
- non-constructor : 메서드, 화살표 함수

```javascript
/* ---constructor--- */
// 함수 선언문
function foo() {}
const bar = function() {};
// 함수를 프로퍼티 값으로 사용하면 일반적으로 메서드로 통칭한다.
// 그러나 ECMAScirpt 사양에서 메서드란 ES6의 메서드 축약 표현만을 의미한다.
// 프로퍼티에 할당된 것은 일반 함수로 정의된 함수이다. 이는 메서드가 아니다.
const hey = {
    prop: function() {}
};

/* ---non-constructor--- */
const arrow = () => {};

const obj = {
    prop() {}
};
```


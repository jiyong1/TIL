# [JS] 프로미스

자바스크립트는 비동기 처리를 위한 하나의 패턴으로 **콜백 함수**를 사용한다. 하지만 콜백 패턴은 **콜백 헬**로 인해 가독성이 나쁘고 비동기 처리 중 발생한 에러의 처리가 곤란하며 여러 개의 비동기 처리를 한번에 하는데도 한계가 있다.

위와 같은 단점을 보완하기 위해서 ES6에서 비동기 처리를 위한 패턴으로 **프로미스(Promise)**를 도입했다. 프로미스는 콜백 패턴의 단점을 보완하고 비동기 처리 시점을 명확하게 표현할 수 있다는 장점이 있다.

<br>

## 1. 프로미스의 생성

`Promise`생성자 함수를 new 연산자와 함께 호출하면 프로미스 객체를 생성한다. Promise는 호스트 객체가 아닌 ECMAScript 사양에 정의된 표준 빌트인 객체이다.

```javascript
// GET 요청을 위한 비동기 함수
const promiseGET = url => {
    return new Promise((resolve, reject) => {
        const xhr = new XMLHttpRequest();
        xhr.open('GET', url);
        xhr.send();
        
        xhr.onload = () => {
            if(xhr.status === 200) {
                resolve(JSON.parse(xhr.response));
            } else {
                reject(new Error(xhr.status));
            }
        };
    });
};

// promiseGET 함수는 promise를 반환한다.
promiseGET('...')
```

<br>

프로미스는 다음과 같이 현재 비동기 처리가 어떤 상태인지 상태 정보를 갖는다.

| 프로미스의 상태 정보 | 의미                                  | 상태 변경 조건                   |
| -------------------- | ------------------------------------- | -------------------------------- |
| pending              | 비동기 처리가 아직 수행되지 않은 상태 | 프로미스가 생성된 직후 기본 상태 |
| fulfilled            | 비동기 처리가 수행된 상태 - 성공      | resolve 함수 호출                |
| rejected             | 비동기 처리가 수행된 상태 - 실패      | reject 함수 호출                 |

<br>

## 2. 프로미스의 후속 처리 메서드

프로미스의 비동기 처리 상태가 변화하면 이에 따라 후속 처리를 해야한다. 예를 들어, 프로미스가 fulfilled 상태가 되면 프로미스의 처리 결과를 가지고 무언가를 해야 하고, 프로미스가 rejected가 되면 프로미스의 처리 결과를 가지고 에러 처리를 해야한다.

<br>

### 2.1 Promise.prototype.then

then 메서드는 두 개의 콜백 함수를 인수로 전달받는다.

1.  첫 번째 콜백 함수는 프로미스가 fulfilled 상태가 되면 호출된다. 이때 콜백 함수는 프로미스의 비동기 처리 결과를 인수로 전달받는다.
2. 두 번째 콜백 함수는 프로미스가 rejected 상태가 되면 호출된다. 이때 콜백 함수는 프로미스의 에러를 인수로 전달받는다.

보통 catch를 사용하기 때문에 의아해 할 수 있으나 catch를 사용하는 것이 일반적이고, 원래 catch 메서드를 호출하면 내부적으로 then()을 호출한다.

```javascript
new Promise(resolve => resolve('fulfilled'))
.then(res => console.log(res), err => console.error(err))
```

then 메서드는 **언제나 프로미스를 반환한다.** 만약 then 메서드의 콜백 함수가 프로미스가 아닌 값을 반환하면 그 값을 암묵적으로 resolve 또는 reject하여 프로미스를 생성해 반환한다.

<br>

## 2.2 Promise.prototype.catch

catch 메서드의 콜백 함수는 프로미스가 rejected 상태인 경우만 호출된다.

```javascript
new Promise((_, reject) => reject(new Error('hi')))
.then(undefined, err => console.log(err))

// catch
new Promise((_, reject) => reject(new Error('hi')))
.catch(err => console.log(err))
```

catch 메서드는 `then(undefined, onRejected)`와 동일하게 동작한다. 따라서 then과 마찬가지로 프로미스를 반환한다.

<br>

## 2.3 Promise.prototype.finally

finally 메서드는 하나의 콜백 함수를 인수로 받는다. finally 메서드의 콜백 함수는 프로미스의 성공, 실패와 상관 없이 무조건 호출된다. (이름과 같이..) 또한 then/catch와 마찬가지로 언제나 프로미스를 반환한다.

```javascript
new Promise((_, reject) => reject(new Error('hi')))
.catch(err => console.log(err))
.finally(() => console.log('bye'))

/*
Error: hi
    at C:\Users\ji yong kim\Desktop\js\test.js:5:35
    at new Promise (<anonymous>)
    at Object.<anonymous> (C:\Users\ji yong kim\Desktop\js\test.js:5:1)
    at Module._compile (internal/modules/cjs/loader.js:1063:30)
    at Object.Module._extensions..js (internal/modules/cjs/loader.js:1092:10)
    at Module.load (internal/modules/cjs/loader.js:928:32)
    at Function.Module._load (internal/modules/cjs/loader.js:769:14)
    at Function.executeUserEntryPoint [as runMain] (internal/modules/run_main.js:72:12)
    at internal/main/run_main_module.js:17:47
bye
*/
```

<br>

## 3. 프로미스 체이닝

프로미스 메서드(then, catch, finally)는 언제나 프로미스를 반환하기 때문에 (반환하지 않더라도 암묵적으로 resolve 또는 reject하여 프로미스를 생성해 반환한다.) 연속적으로 호출할 수 있다. 이를 **프로미스 체이닝 (promise chaining)**이라고 한다.

프로미스는 프로미스 체이닝을 통해 비동기 처리 결과를 전달받아 후속 처리를 하므로 콜백 패턴에서 발생하던 **콜백 헬**이 발생하지 않는다. 하지만 프로미스도 콜백 패턴을 사용하므로 콜백 함수를 사용하지 않는 것은 아니다. 결국 가독성이 안좋은건 동일하다..

이러한 문제를 해결하기 위해 ES8에서 도입된 **async/await**를 통해 해결할 수 있다.

<br>

## 4. 마이크로태스크 큐

```javascript
setTimeout(() => console.log(1), 0)

new Promise(resolve => resolve(2))
.then(res => {
    console.log(res)
    return 3
})
.then(res => {
    console.log(res)
})

/*
2
3
1
*/
```

프로미스 후속 처리 메서드도 비동기로 처리하므로 1, 2, 3 순으로 출력될 것처럼 보이지만 **2, 3, 1** 순으로 출력된다. 그 이유는 프로미스의 후속 처리 메서드의 콜백 함수는 태스크 큐가 아닌 **마이크로태스크 큐**에 저장되기 때문이다.

마이크로태스크 큐는 태스크 큐와 별도의 큐로 프로미스의 후속 처리 메서드의 콜백 함수가 일시 저장된다. 그 외의 비동기 함수의 콜백 함수나 이벤트 핸들러는 태스크 큐에 일시 저장된다.

**마이크로태스크 큐는 태스크 큐보다 우선순위가 높다**. 즉, 이벤트 루프는 콜 스택이 비면 먼저 마이크로태스크 큐에서 대기하고 있는 함수를 가져와 실행한다. 이후, 마이크로태스크 큐가 비면 태스크 큐에 대기하고 있는 함수를 가져와 실행한다.

<br>

## 5. fetch

fetch함수는 XMLHttpRequest 객체와 마찬가지로 HTTP 요청 전송 기능을 제공하는 클라이언트 사이드 Web API이다. fetch 함수는 사용법이 더 간단하고 프로미스를 지원하기 때문에 비동기 처리를 위한 콜백 패턴의 단점에서 자유롭다.

fetch 함수에는 HTTP 요청을 전송할 URL과 HTTP 요청 메서드, HTTP 요청 헤더, 페이로드 등을 설정한 객체를 전달한다.

fetch 함수는 HTTP 응답을 나타내는 Response 객체를 래핑한 Promise 객체를 반환한다.

```javascript
fetch('https://jsonplaceholder.typicode.com/todos/1')
// res는 HTTP 응답을 나타내는 Response 객체이다.
.then(res => {
    console.log(res)
    return res.json()
})
.then(json => console.log(json))
.catch(err => console.error(err))
```


# [JS] async/await

ES8(ECMAScript 2017)에서는 비동기 처리를 동기 처리처럼 동작하도록 구현할 수 있는 `async/await`가 도입되었다.

async/await는 프로미스를 기반으로 동작한다. async/await 를 사용하면 then, catch, finally 후속 처리 메서드를 사용할 필요 없이 마치 동기 처럼 프로미스를 사용할 수 있다.

```javascript
async function asyncFunc() {
    // url이 있다고 가정
    // fetch 함수를 사용하면 promise 객체가 반환된다.
    const response = await fetch(url);
    const toJson = await response.json();
    console.log(toJson);
}

asyncFunc();
```

<br>

## 1. async 함수

await 키워드는 async 함수 내에서 사용해야 한다. async 함수는 async 키워드를 사용해 정의하며 언제나 프로미스를 반환한다. async 함수가 명시적으로 프로미스를 반환하지 않더라도 암묵적으로 resolve하는 프로미스를 반환한다.

```javascript
async function foo(n) {return n;}
foo(1).then(res => console.log(res)) // 1
```

<br>

## 2. await 키워드

await 키워드는 프로미스가 settled 상태 (비동기 처리가 수행된 상태)가 될 때까지 대기하다가 settled 상태가 되면 프로미스가 resolve한 처리 결과를 반환한다. await 키워드는 반드시 프로미스 앞에 사용해야 한다.

```javascript
async function foo() {
    const x = await 1; // 'await'는 이 식의 형식에 영향을 주지 않습니다.
}
```

<br>

```javascript
async function foo() {
    const a = await new Promise(resolve => setTimeout(() => resolve(1), 3000));
    const b = await new Promise(resolve => setTimeout(() => resolve(2), 3000));
    const c = await new Promise(resolve => setTimeout(() => resolve(3), 3000));
    
    console.log(a, b, c);
    
}

foo(); // 9초 후 1 2 3 이 출력된다.
```

모든 프로미스에 await 키워드를 사용하는 것을 주의해야 한다. 위의 예시는 서로 연관이 없어 개별적으로 수행되는 비동기 처리이므로 앞의 비동기 처리가 완료될 때까지 대기할 필요가 없다. 따라서 다음과 같이 처리한다.

```javascript
async function foo() {
    const all = await Promise.all([
        new Promise(resolve => setTimeout(() => resolve(1), 3000)),
        new Promise(resolve => setTimeout(() => resolve(2), 3000)),
        new Promise(resolve => setTimeout(() => resolve(3), 3000)),
    ])

    console.log(all);
}

foo(); // 약 3초 후 [1, 2, 3]이 출력된다.
```

await 키워드는 **앞선 비동기 처리의 결과를 가지고 다음 비동기 처리를 수행해야 하는 경우** 사용하여 순차적으로 처리하게 하는 것이다.

<br>

## 3. 에러 처리

비동기 처리를 위한 콜백 패턴의 단점 중 하나는 에러 처리가 곤란하다는 것이다. 에러는 **호출자** 방향으로 전파된다. 즉, 콜 스택의 아래 방향으로 전파된다. 하지만 비동기 함수의 콜백 함수를 호출하는 것은 비동기 함수가 아니기 때문에 try catch문을 사용해 에러를 캐치할 수 없다.

```javascript
try {
    setTimeout(() => {
        throw new Error('hi');
    }, 1000);
} catch (err) {
    // 에러를 캐치하지 못한다.
    console.error('에러 잡았다', err);
}

/*
C:\Users\ji yong kim\Desktop\js\test.js:3
        throw new Error('hi');
        ^

Error: hi
    at Timeout._onTimeout (C:\Users\ji yong kim\Desktop\js\test.js:3:15)
    at listOnTimeout (internal/timers.js:554:17)
    at processTimers (internal/timers.js:497:7)
*/
```

<br>

async/await에서 에러 처리는 위와 다르게 try catch문을 사용할 수 있다. 콜백 함수를 인수로 전달받는 비동기 함수와 다르게 프로미스를 반환하는 비동기 함수는 명시적으로 호출할 수 있기 때문에 호출자가 명확하다.

또한 async 함수 내에서 **try catch 문을 사용해서 에러 처리를 하지 않으면 async 함수는 발생한 에러를 reject하는 프로미스를 반환한다.** 따라서 후속 처리 메서드 catch를 사용해 에러를 캐치할 수도 있다.
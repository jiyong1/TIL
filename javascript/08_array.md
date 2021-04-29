# [JS] 배열

> 자바스크립트에 배열이라는 타입은 존재하지 않는다. 배열은 객체 타입이다.

자바스크립트에서 배열은 객체이지만 일반 객체와 구별되는 독특한 특징이 있다.

<br>

| 구분      | 객체                      | 배열          |
| --------- | ------------------------- | ------------- |
| 구조      | 프로퍼티 키와 프로퍼티 값 | 인덱스와 요소 |
| 값의 참조 | 프로퍼티 키               | 인덱스        |
| 값의 순서 | X                         | O             |
| length    | X                         | O             |

<br>

## 자바스크립트 배열은 배열이 아니다.

배열은 일반적으로 동일한 크기를 갖는 메모리 공간이 연속적으로 나열된 자료구조를 말한다. 이러한 배열을 **밀집 배열**이라고 한다.

이러한 배열은 인접해서 위치해 있기 때문에, **요소에 효율적으로 접근할 수 있다는 장점이 있다.** 하지만, 정렬되지 않은 배열에서 특정한 요소를 검색하는 경우 모든 요소를 처음부터 발견할 때까지 검색해야한다. (시간 복잡도 O(N))

그리고 요소를 삭제하거나 추가할 때 배열의 요소들을 연속적으로 유지하기 위해 요소들을 이동시켜야하는 단점도 있다.

하지만 자바스크립트의 배열은 요소 각각의 메모리 공간이 동일하지 않을 수 있고, 연속적으로 이어져 있지 않을 수 있다. 이처럼 배열의 요소가 연속적으로 이어져 있지 않는 배열을 **희소 배열(Sparse array)**라고 한다.

즉, 자바스크립트의 배열은 배열의 동작을 따라하는 특수한 객체인 것이다.

<br>

## 희소 배열

희소 배열은 요소가 연속적으로 위치하지 않고 일부가 비어 있는 배열을 희소 배열이라고 한다.

자바스크립트는 희소 배열을 허용한다.

```javascript
const sparseArr = [, 2, , 4];

console.log(sparseArr.length); // 4
console.log(sparseArr); // [empty, 2, empty, 4]
```

<br>

## 배열 생성

<br>

### 배열 리터럴

> 0개 이상의 요소를 쉼표로 구분하여 대괄호 ([])로 묶는다.

```javascript
const arr = [1, 2, 3];
```

<br>

### Array 생성자

> Array 생성자 함수를 이용하여 배열을 생성할 수 있다.

```javascript
const arr = new Array(4);

console.log(arr); // [empty x 4]
```

```javascript
// 인수가 숫자가 아니거나 2개 이상이면 인수를 요소로 갖는 배열을 생성한다.
const arr = new Array(1, 2, 3);

console.log(arr;) // [1, 2, 3]
```

<br>

### Array of

> Array 생성자 함수와는 다르게 인수가 숫자이고 한개이더라도 인수를 요소로하는 배열을 만든다.

```javascript
const arr = Array.of(1);

console.log(arr) // [1]
```

<br>

### Array from

> 유사 배열객체 또는 iterable 객체를 인수로 받아 배열로 변환하여 반환한다.

```javascript
const arr = Array.from('jiyong') // ['j', 'i', 'y', 'o', 'n', 'g']

// 설명하기 위해 같은 변수명을 입력한 것이다. 사실 const는 같은 변수명을 입력하면 오류가 발생한다.
const arr = Array.from({length: 3}, (_, i) => i); // [1, 2, 3]
```

<br>

## 배열 요소의 추가

자바스크립트 객체에 프로퍼티를 동적으로 추가할 수 있는 것처럼 배열에도 요소를 동적으로 추가할 수 있다.

즉, 존재하지 않는 인덱스를 사용해 값을 할당하면 새로운 요소가 추가된다. length 프로퍼티도 자동으로 갱신된다.

```javascript
const arr = [1];
arr[1] = 2;

console.log(arr.length) // 2
```

```javascript
const arr = [1, 2, 3];
arr[99] = 100;

console.log(arr.length) // 100 (희소 배열 !!)
```

<br>

## 배열 요소 삭제

배열은 객체이기 때문에 특정 요소를 삭제하기 위해 delete 연산자를 사용할 수 있다.

```javascript
const arr = [1, 2, 3];

delete arr[1];

console.log(arr) // [1, empty, 3]
console.log(arr.length) // 3 -> length 프로퍼티는 갱신되지 않는다. 희소 배열이 된다 !
```

<br>

## 배열 메서드

> 자바스크립트 배열 빌트인 메서드

Array 생성자 함수는 정적 메서드를 제공하며, 배열 객체의 프로토타입 `Array.prototype`은 프로토타입 메서드를 제공한다.

<br>

### Array.isArray

> 전달된 인수가 배열인가 아닌가?

```javascript
// true
Array.isArray([]);
Array.isArray(Array.of(1));

// false
Array.isArray(1);
Array.isArray('Array');
```

<br>

### Array.prototype.indexOf

> 원본 배열에서 인수로 전달된 요소를 검색하여 인덱스를 반환한다.
>
> 존재하지 않는다면 -1을 반환한다.

```javascript
const arr = [1, 2, 3,];

arr.indexOf(2); // 1
arr.indexOf(4); // -1
```

<br>

### Array.prototype.push

> 인수로 전달받은 모든 값을 원본 배열의 마지막 요소로 추가한다.
>
> 변경된 length 프로퍼티를 반환한다.

```javascript
const arr = [1, 2, 3];

let newLength = arr.push(4, 5);
console.log(newLength); // 5
```

- 원소 값을 하나 추가할 때는 push 보다는 다음과 같이 하는 것이 성능면에서 좋다.

```javascript
const arr = [1, 2, 3];

arr[arr.length] = 4;
```

- ES6의 스프레드 문법을 사용하는 것이 더 좋다.

```javascript
const arr = [1, 2, 3];

const newArr = [...arr, 4];
console.log(newArr); // [1, 2, 3, 4]
```

<br>

### Array.prototype.pop

>  마지막 요소를 원본 배열에서 제거하고 제거한 요소를 반환한다.

```javascript
const arr = [1, 2, 3];

console.log(arr.pop()); // 3 
console.log(arr); // [1, 2]
```

<br>

#### push, pop을 이용한 Stack 자료구조 구현

```javascript
class Stack {
    #array;
    
    constructor(array = []){
        if (!Array.isArray(array)) {
            throw new TypeError(`${array} is not an array`);
        }
        this.#array = array;
    }
	
	push(value) {
        return this.#array.push(value);
    }
	
	pop(value) {
        return this.#array.pop();
    }
	
	// 원본 배열 복사본 반환
	entries() {
        return [...this.#array];
    }
}

const s = new Stack();
s.push(1);

console.log(s.entries()); // [1]
s.push(2);
console.log(s.pop()) // 2
```

<br>

### Array.prototype.unshift

> 인수로 전달받은 값을 원본 배열의 앞에 요소로 추가하고 변경된 length 프로퍼티 값을 반환한다.

```javascript
const arr = [1, 2];

console.log(arr.unshift(3, 4)); // 4
console.log(arr) // [3, 4, 1, 2]
```

<br>

### Array.prototype.shift

> 첫 번째 요소를 제거하고 제거한 요소를 반환한다.

```javascript
const arr = [1, 2, 3, 4];

console.log(arr.shift()); // 1
console.log(arr); // [2, 3, 4]
```

<br>

### Array.prototype.splice

> 원본 배열의 중간에 요소를 제거하고 인자로 전달된 값을 추가한다.
>
> 제거된 요소가 배열로 반환된다.

```javascript
const arr = [1, 2, 3];

const result = arr.splice(1, 1, 3, 4); // 인덱스 1부터 1개의 요소를 제거하고 3, 4을 추가한다.
// 배열로 반환된다.

console.log(result); // 2
console.log(arr;) // [1, 3, 4, 3]

arr.splice(1, 0, 5); // 인덱스 1부터 0개 요소를 제거하고 5를 추가한다.
arr.splice(1, 2); // 인덱스 1부터 2개 요소를 제거하고 아무것도 추가하지 않는다.
```

<br>

### Array.prototype.slice

> 인수로 전달된 범위의 요소들을 복사하여 배열로 반환한다.
>
> 원본은 변경되지 않는다.

```javascript
const arr = [1, 2, 3];

arr.slice(1, 2); // arr[1] ~ arr[2]이전 (arr[2] 미포함) 까지 복사하여 반환한다.

arr.slice(1); // 인수 한개는 1 이후 부터 모두 복사

arr.slice(-1); // 음수인 경우 끝에서부터 요소를 복사 [3]
arr.slice(-2); // [2, 3]

arr.slice(); // 인수가 없는 경우 복사본 생성 [1, 2, 3] (shallow copy)
```

<br>

### Array.prototype.join

> 원본 배열의 모든 요소를 문자열로 변환 후, 구분자로 연결
>
> 구분자 default = ','

```javascript
const arr = [1, 2, 3];

arr.join(); // 1,2,3
arr.join('') // 123
```

<br>

### Array.prototype.reverse

> 원본 배열의 순서를 반대로 뒤집는다. 반환 값또한 변경된 배열

```javascript
const arr = [1, 2, 3];
const newArr = arr.reverse();

console.log(arr); // [3, 2, 1]
console.log(newArr); // [3, 2, 3]
```

<br>

### Array.prototype.fill

> 배열의 처음부터 끝까지 인수로 전달받은 값으로 채운다.

```javascript
const arr = [1, 2, 3]
arr.fill(0);

console.log(arr) // [0, 0, 0]
```

<br>

### Array.prototype.includes

> 배열에 인수로 전달받은 값이 존재하는지 여부를 출력한다.

```javascript
const arr = [1, 2, 3]

console.log(arr.includes(2)); // true
```

<br>

### Array.prototype.flat

> ES10에서 도입된 flat 메서드
>
> 인수로 전달받은 값의 깊이만큼 재귀적으로 배열을 평탄화 한다.

```javascript
const arr = [1, [2, 3, 4, 5]]
console.log(arr.flat()) // [1, 2, 3, 4, 5]

const arr2 = [1, [2, [3, [4, [5]]]]];
console.log(arr2.flat(2)); // [1, 2, 3, [4, [5]]]
```

<br>

### Array.prototype.sort

> 많이 봤듯.. 정렬하는 함수이다.
>
> 오름차순 정렬으로, 내림차순으로 사용하고 싶은경우 reverse 메서드를 사용하여 요소의 순서를 뒤집는다.

<br>

### Array.prototype.forEach

> 요소 하나하나 돌면서 콜백 함수를 실행한다.

```javascript
const arr = [1, 2, 3];
const double = [];

arr.forEach(item => {double[double.length] = item * 2});
console.log(double); // [2, 4 ,6]
```

<br>

### Array.prototype.map

> 콜백 함수의 반환값들로 구성된 새로운 배열을 반환한다.

`forEach`는 반환하지 않아서 직접 push (엄밀히 말하면 push 함수를 사용한 것은 아니지만..)한 것을 볼 수 있다.

```javascript
const arr = [1, 2, 3];
const double = arr.map(item => item * 2);

console.log(double); // [2, 4, 6]
```

<br>

### Array.prototype.filter

> 모든 요소를 순회하면서 콜백 함수를 호출한다. 콜백 함수의 반환 값이 true인 요소로만 구성된 새로운 배열을 반환한다.

```javascript
const arr = [1, 2, 3, 4]
const oddArr = arr.filter(item => item % 2);

console.log(oddArr); // [1, 3]
```

<br>

### Array.prototype.reduce

> 모든 요소를 순회하면서 누적된 값을 첫 번째 인수로 전달받아 결과적으로 하나의 결과값을 만들어 반환한다.
>
> 원본 배열은 변경되지 않는다.

```javascript
const arr = [1, 2, 3, 4];
const sum = arr.reduce((acc, item) => acc + item);

console.log(sum) // 10
```

```javascript
const arr = [1, 2, 3, 4, 5];
const avg = arr.reduce((acc, item, index, { length }) => {
    return index === length - 1 ? (acc + item) / length : acc + item;
});

console.log(avg); // 3
```

<br>

### Array.prototype.some

> 배열의 모든 요소를 순회하면서 콜백 함수의 반환 값이 하나라도 true이면 true를 반환한다.

```javascript
const arr = [1, 2, 3]

console.log(arr.some(item => item >= 3)) // true
```

<br>

### Array.prototype.every

> 배열의 모든 요소를 순회하면서 콜백 함수의 반환 값이 모두 true이면 true를 반환한다.

```javascript
const arr = [1, 2, 3]

console.log(arr.every(item => item >= 3)) // false
```

<br>

### Array.prototype.find

> ES6에 도입된 find 메서드
>
> 배열의 요소를 순회하면서 콜백 함수의 반환 값이 처음으로 true가 나온 요소를 반환한다.

```javascript
const users = [
    {id: 1, name: 'kim'},
    {id: 2, name: 'lee'},
    {id: 3, name: 'park'},
	{id: 4, name: 'lee'},
]

console.log(users.find(user => user.name === 'lee')) // { id: 2, name: 'lee' }
```

<br>

### Array.prototype.findIndex

> 위와 동일하지만 요소가 아닌 index를 반환한다.
>
> 없으면 -1 반환

```javascript
const users = [
    {id: 1, name: 'kim'},
    {id: 2, name: 'lee'},
    {id: 3, name: 'park'},
	{id: 4, name: 'lee'},
]

console.log(users.findIndex(user => user.name === 'lee')) // 1
```

<br>


# Object



```javascript
const Person = {
    name: '지용',
    age: '20',
    introduce function() {
        console.log('안녕하세요? 저는 ' + this.name + '입니다. 나이는 ' + this.age + '입니다.');
    }
}
```



## 생성자

- 생성자 (Constructor)

  ```javascript
  function Person(name, age) {
      this.name = name;
      this.age = age;
      this.introduce = function() {
          console.log('안녕하세요? 저는 ' + this.name + '입니다. 나이는 ' + this.age + '입니다.');
      }
  }
  
  const person1 = new Person('지용', 20);
  const person2 = new Person('용김', 21);
  ```

  - person1, person2 : `instance`
  - 메모리 낭비.. introduce와 같은 경우 각각 보유하고 있다.



## Prototype

- prototype 사용시 instance가 늘어난다고 해서 **introduce 인스턴스 메서드가 늘어나지 않는다.**

```javascript
Person.prototype.introduce = function() {
    console.log('안녕하세요? 저는 ' + this.name + '입니다. 나이는 ' + this.age + '입니다.');
};
```



- **공통되는 애들은 prototype**으로 선언해주면 된다.

```javascript
function Card(num, shape){
    this.num = num
    this.shape = shape
}

Card.prototype.width = 100;
Card.prototype.height = 150;

/* ----다른 방법---- */

Card.prototype = {
    constructor: Card,
    init: function() {
        //..//
    }
}
```

- num, shape는 각각 보유
- 너비와 높이는 동일한 카드 !


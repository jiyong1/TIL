# 02. react

> props와 state

<br>

- 리액트 컴포넌트에서 다루는 데이터는 두개로 나뉩니다.
  - `props`
  - `state`

<br>

## props

<br>

### 새 컴포넌트 만들기

> MyName 이라는 컴포넌트를 만들어 보자.

<br>

```jsx
import React, { Component } from 'react';

class MyName extends Component {
  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

export default MyName;
```

```jsx
// App.js
import React, { Component } from 'react';
import MyName from './MyName';

class App extends Component {
  render() {
    return <MyName name="김지용" />;
  }
}

export default App;
```

- 자신이 받은 props value는 `this.` 키워드를 통해 조회할 수 있다.

<br>

---



### defaultProps

> 특정 상황에서나 실수로 props를 선언하지 않을 수 있다.
>
> 이러한 경우 default 값을 설정하여 default 값이 출력되게 할 수 있다.

<br>

```jsx
// MyName.js

import React, { Component } from 'react';

class MyName extends Component {
  static defaultProps = {
    name: '기본이름'
  }

  render() {
    return (
      <div>
        안녕하세요! 제 이름은 <b>{this.props.name}</b> 입니다.
      </div>
    );
  }
}

export default MyName;
```

```jsx
// App.js

import React, { Component } from 'react';
import MyName from './MyName';

class App extends Component {
  render() {
    return <MyName />;
  }
}

export default App;
```

<br>

---

<br>

### 함수형 컴포넌트

```jsx
// MyName.js
import React from 'react';

const MyName = ({ name }) => {
  return <div>안녕하세요 제 이름은 {name} 입니다.</div>;
};

MyName.defaultProps = {
  name: '지용이'
};

export default MyName;
```

- 코드 상단에서 `{ Component }` 를 import 할 필요 없다.
- `MyName` 은 **비구조화 할당 문법**
- 함수형 컴포넌트는 `state`와 `LifeCycle`이 빠져 있다.
  - 그래서 컴포넌트 초기 마운트가 아주 미세하게 빠르고, 메모리 자원을 덜 사용한다.
  - 컴포넌트를 무수히 많이 렌더링 하는게 아니라면 사실상 큰 차이 없다..

<br>

## state

> `props` 는 부모가 자식한테 내리고, 읽기 전용이다.
>
> `state`는 내부에서 변경 할 수 있다.
>
> 동적인 데이터를 다룰 때 사용한다.

<br>

```jsx
import React, { Component } from 'react';

class Counter extends Component {
    // state
    state = {
        number: 0
    }
	
	// 화살표 함수 사용
	handleIncrease = () => {
        this.setState({
            number = this.state.number + 1
        });
    }
    
    handleDecrease = () => {
        this.setState({
            number = this.state.number - 1
        });
    }
    
    render(){
        return (
        	<div>
            	<h1>카운터</h1>
                <div>값: {this.state.number}</div>
                <button onClick={this.handleIncrease}>+</button>
                <button onClick={this.handleDecrease}>-</button>
            </div>
        );
    }
}
```

- 컴포넌트의 state를 정의할 때는 `class fields` 문법을 사용한다.
- 만약 `constructor`를 작성했을 때는 Component를 상속해야 한다.
  - 기존의 클래스 생성자를 덮어쓰게 되므로..
- 컴포넌트의 메서드는 `화살표 함수`로 작성해야 한다.
  - 그렇지 않으면 `this`와의 연결이 끊겨버린다..
  - 물론 연결 해주는 방법은 있다..!

<br>

```jsx
class Counter extends Component{
    state = {
        number: 0
    };
	
	// constructor 사용
	constructor(props) {
        super(props);
        // bind(연결) 해주기
        this.handleIncrease = this.handleIncrease.bind(this);
        this.handleDecrease = this.handleDecrease.bind(this);
    }
	
	handleIncrease(){
        this.setState({
            number = this.state.number + 1
        });
    }
    
    handleDecrease(){
        this.setState({
            number = this.state.number - 1
        });
    }
}
```



<br>

### setState

> state 값을 바꾸기 위해서는  setState를 무조건 거쳐야 한다.

<br>

```jsx
state = {
    number: 0;
}

this.setState({
    number: this.state.number + 1
});
```

<br>

- **!!주의할 점!!**
- `setState`는 객체의 깊은 곳까지 들어가지 않는다.

```jsx
state = {
    number: 0,
    foo: {
      bar: 0,
      foobar: 1
    }
}

this.setState({
  foo: {
    foobar: 2
  }
})
```

- 위와 같이 하게 되면 **foo 객체 자체가 변경된다.**
- 따라서 다음과 같이 해주어야 한다.

```jsx
this.setState({
  number: 0,
  foo: {
    ...this.state.foo,
    foobar: 2
  }
});
```

- `...` 은 자바스크립트의 **전개연산자** 이다.
  - 객체안의 내용을 작성된 위치에 풀어준다는 의미!!



<br>

- `비구조화 할당`으로 작성하기
  - 좀 더 멋진 문법으로 작성해본다..

```jsx
handleIncrease = () => {
    const { number } = this.state;
    this.setState({
        number: number + 1
    });
}

handleDecrease = () => {
    this.setState(
        /*
        (state) => ({
        	number: state.number - 1
        })
        */
    	({number}) => ({
            number: number - 1
        })
    );
}
```

<br>

- 이벤트이름을 설정할 때 **camelCase**로 설정해야 한다.
  - `onclick : onClick`
  - `onmousedown : onMouseDown`
  - ...



<br>


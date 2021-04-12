# 01. react

> JSX 기본 문법 알아보기

<br>

- react를 사용하면 웹 어플리케이션에서 사용하는 유저 인터페이스를 재사용 가능한 컴포넌트로 분리하여 작성함으로서, 프로젝트의 유지보수성을 우수하게 해준다.

<br>

## 감싸져 있는 엘리먼트

<br>

- 두개 이상의 엘리먼트는 무조건 하나의 엘리먼트로 감싸져 있어야 한다.
- 스타일 관련 설정을 하면서 코드가 꼬이게 될 수도 있는 등 번거로운 일이 생길 수 있다.
  - `Fragment` 사용!

<br>

## JSX 안에 자바스크립트 값 사용하기

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    const name = 'react';
    return (
      <div>
        hello {name}!
      </div>
    );
  }
}

export default App;
```

<br>

### var, const, let

- var
  - scope가 함수 단위 이다.
  - ES6 에서는 var을 사용하지 않는다.
- const
  - scope가 블록 단위이다.
  - 값을 선언 후, 변경하지 않을 때 사용
- let
  - scope가 블록 단위이다.
  - 값 선언 후, 변경 할 때 사용!

<br>

---

<br>

## 조건부 렌더링

> JSX 내부에서 조건부 렌더링을 할 때는 보통 삼항 연산자를 사용하거나, AND 연산자를 사용합니다.

<br>



```jsx
import react, { Component } from 'react';

class App extends Component {
    render(){
        return (
        	<div>
            	{
                    1 + 1 === 2
                    ? '맞다'
                    : '틀리다'
                }
            </div>
        )
    }
}
```

```jsx
import react, { Component } from 'react';

class App extends Component {
    render(){
        const name = "지용";
        return (
        	<div>
            	{
                    name === "지용" && <div>지용이네!</div>
                }
            </div>
        )
    }
}
```

<br>

- if 문을 사용하기 위해서는 즉시 실행 함수 (IIFE)를 사용해야 한다.

```jsx
import React, { Component } from 'react';

class App extends Component {
  render() {
    const value = 2;
    return (
      <div>
          {
            (function() {
              if (value === 1) return <div>1이다!</div>
              if (value === 2) return <div>2이다!</div>
              if (value === 3) return <div>3이다!</div>
            })()
          }
      </div>
    )
  }
}

export default App;
```

<br>

## style과 className

```javascript
import React, { Component } from 'react';

class App extends Component {
  render() {
    const style = {
      backgroundColor: 'black',
      padding: '16px',
      color: 'white',
      fontSize: '36px'
    };

    return <div style={style}>안녕하세요!</div>;
  }
}

export default App;
```

<br>

- class

```css
.App {
  background: black;
  color: aqua;
  font-size: 36px;
  padding: 1rem;
  font-weight: 600;
}
```

```jsx
import React, { Component } from 'react';
import './App.css'

class App extends Component {
  render() {
    return (
      <div className="App">
        리액트
      </div>
    );
  }
}

export default App;
```


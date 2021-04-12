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
  const defaultProps = {
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
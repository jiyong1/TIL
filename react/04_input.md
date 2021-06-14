# 04 input 상태 관리하기

<br>

## 프로젝트 생성하기

```bash
create-react-app hello-react
```

해당 디렉토리를 열고 내부에서 `yarn start` 혹은 `npm start`를 통해 개발서버를 시작한다.

<br>

## 컴포넌트 생성과 input 다루기

> src directory 내부에 components directory를 만들어 구분하자.

<br>

```jsx
// src/components/PhoneForm.js
import React, { Component } from 'react';

class PhoneForm extends Component {
  state = {
    name: ''
  }
  handleChange = (e) => {
    this.setState({
      name: e.target.value
    })
  }
  render() {
    return (
      <form>
        <input
          placeholder="이름"
          value={this.state.name}
          onChange={this.handleChange}
        />
        <div>{this.state.name}</div>
      </form>
    );
  }
}

export default PhoneForm;
```

- `handleChange`함수의 매개변수로 이벤트 객체를 받는다.
- `setState`를 이용해 state의 name부분을 이벤트 객체의 value로 지정해준다.
- input 하단에 name의 값이 잘 바뀌는지 확인하도록 `{this.state.name}`을 작성해주었다.

<br>

- 위에서 작성한 컴포넌트를 App에서 보여준다.

```jsx
// src/App.js
import React, { Component } from 'react';
import PhoneForm from './components/PhoneForm';


class App extends Component {
  render() {
    return (
      <div>
        <PhoneForm />
      </div>
    );
  }
}

export default App;
```

<br>

### input이 두개라면?

> 또 다른 이벤트 핸들러 함수를 만드는 것 보다 더 나은 방법이 존재한다!

```jsx
// src/components/PhoneForm.js
import React, { Component } from 'react';

class PhoneForm extends Component {
  state = {
    name: '',
    phone: ''
  }
  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    });
  }
  render() {
    return (
      <form>
        <input
          placeholder="이름"
          value={this.state.name}
          onChange={this.handleChange}
          name="name"
        />
        <input
          placeholder="전화번호"
          value={this.state.phone}
          onChange={this.handleChange}
          name="phone"
        />
        <div>{this.state.name} {this.state.phone}</div>
      </form>
    );
  }
}

export default PhoneForm;
```

- input의 `name`속성을 사용한다.
- 각 name의 값은 `event.target.name` 을 통해서 조회가 가능하다.
- [Computed property names](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Object_initializer#computed_property_names) 문법을 사용하였다.

<br>

### 부모 컴포넌트에게 정보 전달하기

> state 값을 부모 컴포넌트에게 전달하기



1. 부모 컴포넌트에서 메서드 만들기
2. 메서드를 자식에게 전달
3. 자식 내부에서 호출

<br>

![](04_input.assets/react-input.png)

- 출처 : [velopert 블로그](https://velopert.com/3634)

부모(App.js) 에서 `handleCreate` 라는 메서드를 만들고, 이를 `PhoneForm.js`에다가 전달한다.

submit이 발생하면 `props`로 받은 함수를 호출하여 App에서 매개변수로 받은 값을 사용할 수 있다록 한다.

<br>

- 부모 컴포넌트

```jsx
// src/App.js
import React, { Component } from 'react';
import PhoneForm from './components/PhoneForm';

class App extends Component {
  handleCreate = (data) => {
    console.log(data);
  }
  render() {
    return (
      <div>
        <PhoneForm
          onCreate={this.handleCreate}
        />
      </div>
    );
  }
}

export default App;
```

<br>

- 자식 컴포넌트 (PhoneForm.js)

```jsx
// src/components/PhoneForm.js
import React, { Component } from 'react';

class PhoneForm extends Component {
  state = {
    name: '',
    phone: ''
  }
  handleChange = (e) => {
    this.setState({
      [e.target.name]: e.target.value
    })
  }
  handleSubmit = (e) => {
    // 페이지 리로딩 방지
    e.preventDefault();
    // 상태값을 onCreate 를 통하여 부모에게 전달
    this.props.onCreate(this.state);
    // 상태 초기화
    this.setState({
      name: '',
      phone: ''
    })
  }
  render() {
    return (
      <form onSubmit={this.handleSubmit}>
        <input
          placeholder="이름"
          value={this.state.name}
          onChange={this.handleChange}
          name="name"
        />
        <input
          placeholder="전화번호"
          value={this.state.phone}
          onChange={this.handleChange}
          name="phone"
        />
        <button type="submit">등록</button>
      </form>
    );
  }
}

export default PhoneForm;
```

- `e.preventDefault()` : **원래 이벤트가 해야하는 작업을 방지한다**
  - form에서 submit이 발생하면 페이지를 다시 불러오게 되는데, 이를 방지하기 위해서 사용


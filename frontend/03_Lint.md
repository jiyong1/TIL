# [Frontend] 린트

<br>

## 0. 배경

들여쓰기를 맞추지 않고.. 선언한 변수를 어쩌다 보니 사용하지 않는 등.. 이렇게 구성한 코드로 만들어진 어플리케이션이 동작을 하지 않는 것은 아니다. 그러나 코드의 가독성이 떨어지고 코드가 추가될수록 점점 유지보수가 어려운 코드가 될 것이다.

<br>

## 1. ESLint

`ESLint`는 ECMAScript 코드에서 문제점을 검사하고 일부는 더 나은 코드로 정정하는 린트 도구 중의 하나다. **코드의 가독성을 높이고 잠재적인 오류를 제거해 좋은 코드로 만드는 것이 목적이다.**

코드에서 검사하는 항목은 크게 두 가지이다.

- **포맷팅** : 코드를 일관되게 만든다.
- **코드 품질** : 코드의 오류를 사전에 체크해준다.

<br>

### 설치 및 사용법

- 다운로드

  ```bash
  $ npm i eslint
  ```

- ESLint는 기본적으로 환경설정 파일이 필요하다.

  ```javascript
  // .eslintrc.js
  module.exports = {}
  ```

- 실행

  ```bash
  $ npx eslint app.js
  ```

<br>

### 규칙 (Rules)

ESLint는 검사 규칙을 미리 정해 놓았다. [공식 문서](https://eslint.org/docs/rules/)를 통해 규칙 목록을 확인할 수 있다.

<br>

### 자동 수정

다음과 같은 코드가 있다.

```javascript
// app.js
console.log('hi');;;
```

자바스크립트는 원래 여러개의 세미콜론을 사용해도 오류를 출력하지 않는다. 즉 위의 코드는 정상적으로 동작하는 코드이다. 하지만 이것은 코드의 가독성을 나쁘게하는 요소이다.

위 문제에서 사용되는 규칙(Rules)으로 `no-extra-semi` 규칙이 있다.

린트 환경설정 파일에 `no-extra-semi` 규칙을 추가한다.

```javascript
// .eslintrc.js
module.exports = {
    rules: {
        "no-extra-semi": "error",
    },
}
```

<br>

- 빌드

  ```bash
  $ npx eslint app.js
  ```

- 결과

  ```bash
    1:19  error  Unnecessary semicolon  no-extra-semi
    1:20  error  Unnecessary semicolon  no-extra-semi
  
  ✖ 2 problems (2 errors, 0 warnings)
    2 errors and 0 warnings potentially fixable with the `--fix` option.
  ```

<br>

마지막 줄의 메세지를 보면 **potentially fixable (잠재적으로 수정이 가능하다)**이라고 말한다. `--fix` 옵션을 추가해 검사해보자.

```bash
$ npx eslint app.js --fix
```

- 결과

  ```javascript
  // app.js
  console.log('hi');
  ```

<br>

실제로 [공식 문서](https://eslint.org/docs/rules/)에 존재하는 규칙 목록 중 **렌치** 표시가 남겨져 있는 규칙들은 `--fix` 옵션을 추가하여 자동 수정을 할 수 있다.

<br>

### Extensible Config

규칙을 하나하나 적용하는 것이 아니라 미리 정해 놓은 규칙 세트를 사용할 수 있다. - **eslint:recommended**

[공식 문서](https://eslint.org/docs/rules/)의 규칙 목록 중 체크 표시가 되어있는 것이 위 설정에서 활성화되는 규칙이다.

- 환경설정

  ```javascript
  // .eslintrc.js
  module.exports = {
      extends: [
          "eslint:recommended",
      ],
  }
  ```

만약 규칙을 추가하고 싶다면 `rules` 속성을 추가하여 확장할 수 있다.

ESLint에서 제공되는 기본 설정 이외에도 자주 사용되는 것이 두 가지가 있다.

- airbnb
  - [airbnb 스타일 가이드](https://github.com/airbnb/javascript)
  - eslint-config-airbnb-base
- standard
  - [자바스크립트 스탠다드 스타일](https://standardjs.com/)
  - eslint-config-standard

<br>

### 초기화

ESLint 설정 파일은 사실 `--init` 옵션을 추가하여 손쉽게 구성할 수 있다.




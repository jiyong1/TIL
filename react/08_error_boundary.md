# React Error Boundaries

> React 16에서는 에러 경계(Error Boundary)라는 개념이 도입되었다.

error boundary는 하위 컴포넌트 트리의 어디에서는 자바스크립트 에러를 기록하며 깨진 컴포넌트 트리 대신 `fallback` UI를 보여주는 **React Component** 입니다.

- Error Boundary는 다음 에러를 포착하지 않습니다
  1. 이벤트 핸들러
  2. 비동기 코드
  3. 서버사이드 렌더링
  4. 자식이아닌 에러 경계 자체에서 발생하는 에러

<br>

Lifecycle 메서드인 `static getDerivedStateFromError()` 와 `componentDidCatch()` 중 하나 혹은 둘다 정의 하면 클래스 컴포넌트 자체가 **Error boundary** 가 됩니다.

<br>

```jsx
class ErrorBoundary extends React.Component {
  constructor(props) {
    super(props);
    this.state = { hasError: false };
  }
  
  static getDerivedStateFromError(error) {
    // 다음 렌더링에 폴백 UI가 보이도록 상태를 업데이트 합니다.
    return { hasError: true };
  }
  
  componentDidCatch(error, errorInfo) {
    logErrorToMyService(error, errorInfo);
  }
  
  render() {
    if (this.state.hasError) {
      return <h1>error!</h1>;
    }
    
    return this.props.children;
  }
}
```



## react-query 와 QueryErrorResetBoundary

ErrorBoundary 혹은 suspense를 사용한다면 오류가 발생한 후 다시 시도하여 re-rendering 하도록 해주어야 한다.

`QueryErrorResetBoundary` 컴포넌트를 사용하면 boundary내의 어느 쿼리 에러든 reset 할 수 있다.

<br>

```jsx
import { QueryErrorResetBoundary } from 'react-query';
import { ErrorBoundary } from 'react-error-boundary';

const App = () => {
  return (
    <QueryErrorResetBoundary>
       {({ reset }) => (
         <ErrorBoundary
           onReset={reset}
           fallbackRender={({ resetErrorBoundary }) => (
             <div>
               There was an error!
               <Button onClick={() => resetErrorBoundary()}>다시 시도</Button>
             </div>
           )}
         >
           <Page />
         </ErrorBoundary>
       )}
     </QueryErrorResetBoundary>
  )
}
```


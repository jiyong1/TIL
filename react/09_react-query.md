# react-query

> react-query는 React에서 비동기 로직을 쉽게 다루게 해주는 라이브러리

<br>

## react-query의 Global state

- 이젠 **Global State** 가 아니다..!!
  - 전역 state는 Client와 Server로 분류할 수 있고, 두 state 는 다른 방식으로 다뤄져야 효율적인 앱을 만들 수 있다.
- **Server-state 와 Client-state**
  - Client-state : 세션간 지속적이지 않는 데이터, 동기적, 클라이언트가 소유, 항상 최신 데이터로 업데이트
    - ex) 컴포넌트 state
  - Server-state : 세션간 지속되는 데이터, 비동기적, 클라이언트만 소유하는게 아니고 공유되는 데이터도 존재하며 여러 클라이언트에 의해 수정될 수 있음
    - ex) DB에 저장되어 있는 데이터

<br>

## 사용해야할 이유

- React 라이브러리에서 데이터를 fetching 혹은 update하는 옵션을 제공하지 않기 때문에 개발자가 직접 로직을 구현해야 했다.
- 전역 상태 관리 라이브러리를 사용하면 명시적으로 fetching을 수행해야만 최신 데이터를 가져올 수 있다.
- 복수의 컴포넌트가 최신 데이터를 가져오기 위해 여러번 fetching을 하게 되면 네트워크 통신이 여러번 수행되어 비효율적이다.

<br>

## 사용

- App.js에서 Context Provider로 client (queryClient)를 내려보내준다. 

  - 해당 컨텍스트는 앱의 비동기 요청을 알아서 처리하는 **Boundary**가 된다.

    ```jsx
    import { QueryClient, QueryClientProvider } from 'react-query'
     
    const queryClient = new QueryClient()
    
    export default function App() {
      return (
        <QueryClientProvider client={queryClient}>
          <MyApp />
        </QueryClientProvider>
      )
    }
    ```

<br>

### Query

- 쿼리는 비동기 요청을 하여 Promise를 리턴하는 함수와 함께 unique key로 매핑된다.
- unique key는 리패칭, 캐싱, 공유 등을 할 때 참조되는 값이다. 주로 배열을 사용한다.
  - 배열의 요소로 쿼리의 이름을 나타내는 문자열과 프로미스를 리턴하는 함수의 인자로 쓰이는 값을 넣는다.
- Promise를 리턴하는 함수는 반드시 resolve Promise를 리턴하거나 에러를 throw해야 한다.
- useQuery의 반환 값 : isLoading, isError, data, error 등..
  - isIdle : 쿼리 data가 하나도 없고 비었을 때
  - isLoading : 로딩 중
  - Error : 에러 발생

<br>

### Query Key

- 문자열
- 배열
  - query의 정보가 어느 데이터로 인해 unique 하게 표현된다면 배열을 이용하여 표현할 수 있다.
- 두번째 인자로 주어지는 콜백 함수 (비동기 요청 함수) 에서 queryKey에 접근할 수 있다.
- 콜백함수에 주는 인자 : 배열의 마지막 요소이며, 역시 쿼리를 구별하는데 쓰임 ⇒ 엔드포인트가 같더라도 요청에 넣는 body나 쿼리파람이 다르면 다른 쿼리 인스턴스로 취급된다.
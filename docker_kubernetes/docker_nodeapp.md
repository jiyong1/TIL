# Docker를 이용한 Node.js app 만들기

> 아주 아주 아주 간단한 app

<br>

## Express를 이용한 App 만들기

1. project를 만들어준다.

   ```bash
   $ npm init
   ```

2. express 다운로드 하기 !

   ```bash
   $ npm install express
   ```

3. `server.js` 만들기

   ```javascript
   const express = require('express');
   
   const PORT = 8080;
   const HOST = '0.0.0.0';
   
   const app = express();
   
   app.get('/', (req, res) => {
     res.send('Hello World');
   })
   
   app.listen(PORT, HOST);
   console.log(`Running on http://${HOST}:${PORT}`);
   ```

4. **script** 작성

   ```json
   // package.json
   {
     ...
     "scripts": {
       "start": "node server.js"
     }
     ...
   }
   ```

5. 서버 실행 !

   ```bash
   $ npm run start
   ```

6. 잘 되나 확인해봅시다..

   - postman이든 뭐든 좋지만, 개인적으로 vscode extension인 `REST Client` 를 설치하는 것을 추천드립니다
   - `REST Client` 설치 후 통신 보내보기 (`.http` 파일 생성 후 작성)

   ```http
   GET http://0.0.0.0:8080
   ```

- 결과

  ![](/Users/seventwo/Desktop/hello_app.png)

<br>

---

<br>

## Dockerfile 생성

```dockerfile
FROM node:10

RUN npm install

CMD ["node", "server.js"]
```

- 에러가 발생한다..

  - 다른 파일들이 컨테이너 안에 있지 않고, 컨테이너 밖에 있다..!

- `COPY` 를 이용하여 문제를 해결한다!

  ```dockerfile
  FROM node:10
  
  # source dest
  COPY ./ ./
  
  RUN npm install
  
  CMD ["node", "server.js"]
  ```

- 컨테이너 실행

  ```bash
  $ docker run -p 8080:8080 <이미지 이름>
  ```

  - port mapping을 해주어야 하기 때문에 **-p 8080:8080** 을 추가해주어야 한다!
  - 앞 : 로컬 네트워크, 뒤 : 서버의 포트

<br>

---

<br>

## Working Directory

이미지안에서 어플리케이션 소스 코드를 갖고 있을 Directory를 생성하는 것

- 왜 따로 생성해야하는가?
  - copy한 파일들이 root directory에 다 들어오게 된다.
  - 파일이 덮어 씌어질 수 있고, 정리가 안된 느낌..

```dockerfile
FROM node:10

WORKDIR /usr/src/app

COPY ./ ./

RUN npm install

CMD ["node", "server.js"]
```

- workdir을 설정해주면 `ls` 명령을 주면 root directory가 아닌 working directory에 먼저 접근하게 된다.

<br>

---

<br>

## 비효율적인 문제

`COPY ./ ./` 이 부분 때문에 소스 코드가 변경되어도 다시 `npm install` 해야하는 비효율적인 문제가 있다.

캐싱된 데이터를 기반으로 이러한 비효율적인 문제를 해결할 수 있다.

```dockerfile
FROM node:10

WORKDIR /usr/src/app

COPY package.json ./

# 여기까지 캐싱된 데이터를 기반으로 이미지를 만들기 때문에 훨씬 효율적이다.
RUN npm install

COPY ./ ./

CMD ["node", "server.js"]
```

- 소스 코드를 변경하게 되면 `COPY ./ ./` 부터 변경되기 때문에 캐싱된 데이터를 활용하여 좀 더 효율적으로 build 할 수 있다.

<br>

---

<br>

## Docker Volume

- `COPY` : 로컬에 있는 것을 복사하는 것
- `Volume` : **Mapping**

<br>

Volume을 활용하여 어플리케이션을 실행하는 방법

```bash
$ docker run -p 8080:8080 -v /usr/src/app/node_modules -v $(pwd):/usr/src/app
```

- `pwd` : (print working directory)
- 첫번째 `-v` 옵션은 local에 node_modules가 없기 때문에 추가해준 부분
- 두번째 `-v` 옵션은 local의 directory를 container와 mapping 시켜 주려고 하는 부분




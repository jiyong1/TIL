# Docker Image 만들기

- 도커 이미지 생성하는 순서
  1. Dockerfile 작성 : Docker Image를 만들기 위한 설정 파일
  2. 도커 클라이언트 : 도커 파일에 입력된 것들이 도커 클라이언트에 전달되어야 한다.
  3. 도커 서버 : 도커 클라이언트에 전달된 모든 중요한 작업들을 하는 곳
  4. 이미지 생성

<br>

## Docker file

1. 베이스 이미지를 명시해준다.
   - 베이스 이미지 ??
   - 이미지는 여러개의 이미지로 구성되어 있다.
   - 베이스 이미지는 OS라고 생각하면 된다.
2. 추가적으로 필요한 파일을 다운 받기 위한 몇가지 명령어를 명시해준다.
3. 컨테이너 시작시 실행 될 명령어를 명시해준다.

- `From`, `Run`, `CMD`

  ```dockerfile
  # 이미지 생성 시 기반이 되는 이미지 레이어
  # <이미지>:<태그> 형식으로 작성
  # ex) ubuntu:14.04
  FROM baseImage
  
  # Docker Image가 생성되기 전에 수행할 쉘 명령어
  RUN command
  
  # 컨테이너가 시작이 되었을 때 실행할 실행 파일 또는 셸 스크립트
  # 1회만 쓸 수 있다.
  CMD ["executable"]
  ```

- 베이스 이미지는 `ubuntu`를 써도 되고 centos등을 써도 되지만 아주 간단한 app같은 경우는 굳이 사이즈가 큰 베이스 이미지를 사용할 필요가 없다. (`alpine` 베이스 이미지 사용)

<br>

---

<br>

## Build

- 해당 디렉토리 내에서 dockerfile을 찾아서 도커 클라이언트에 전달시켜준다.

  ```bash
  $ docker build ./
  ```

- 이름 정해주기

  ```bash
  $ docker build -t jyong9591/echo:latest
  ```

  - 이름을 적을 때 국룰 같은 것..
    - `<docker id>/<project/repository name>:version`


# 멀티 컨테이너 어플리케이션 만들기 (운영 환경)

1. github master branch push
2. Travis CI
   1. 테스트 코드 실행
   2. 성공 ??
   3. Dockerfile을 통해 image 생성
   4. 이미지 생성 후, Docker Hub로 전달
3. Docker Hub에 저장
4. Elastic Beanstalk에서 가져가려고 하면 전달
5. Elastic Beanstalk을 통해 배포

<br>

## MySQL 도커 환경 정리

AWS RDS를 사용하기 때문에 Docker Compose의 MySQL 도커 환경을 주석처리한다.

<br>

## .travis.yml 작성

```yaml
language: generic

sudo: required

services:
  - docker

before_install:
  - docker build -t jyong9591/react-test-app -f ./frontend/dockerfile.dev ./frontend

script:
  - docker run -e CI=true jyong9591/react-test-app npm run test

after_success:
  - docker build -t jyong9591/multi-frontend ./frontend
  - docker build -t jyong9591/multi-backend ./backend
  - docker build -t jyong9591/multi-nginx ./nginx

  - echo "$DOCKER_HUB_PASSWORD" | docker login -u "$DOCKER_HUB_ID" --password-stdin

  - docker push jyong9591/multi-frontend
  - docker push jyong9591/multi-backend
  - docker push jyong9591/multi-nginx

```

- install 전에 테스트를 한다.
- 테스트 성공 후, docker hub에 image를 push 한다.

<br>

---

<br>

## Dockerrun.aws.json

`dockerfile`이 한개 있을때는 Elastic Beanstalk이 알아서 처리해주었다.

그러나 이제는 frontend, backend, nginx 3가지의 dockerfile이 존재하므로 이를 설정하는 파일이 필요하다! (**Container Definition**)

```json
{
    "AWSEBDockerrunVersion": 2,
    "containerDefinitions": [
        {
            "name": "frontend",
            "image": "jyong9591/multi-frontend",
            "hostname": "frontend",
            "essential": false,
            "memory": 128
        },
        {
            "name": "backend",
            "image": "jyong9591/multi-backend",
            "hostname": "backend",
            "essential": false,
            "memory": 128
        },
        {
            "name": "nginx",
            "image": "jyong9591/multi-nginx",
            "hostname": "nginx",
            "essential": true,
            "portMappings": [
                {
                    "hostPort": 80,
                    "containerPort": 80
                }
            ],
            "links": ["frontend", "backend"],
            "memory": 128
        }
    ]
}
```

- `name` : container의 이름
- `image` : docker container를 구축할 온라인 docker repository의 이름
- `hostname` : 이 이름을 이용해서 컨테이너간의 접근이 가능해진다.
- `essential` : 컨테이너가 실패할 경우 작업을 멈춰야하는지 ?!
- `memory` : 한 컨테이너에서 얼마나 많은 메모리를 소모할 것인지
- `portMappings` : 컨테이너의 네트워크와 host 네트워크를 매핑합니다.
- `links` : 연결할 컨테이너의 목록
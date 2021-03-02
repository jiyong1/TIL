# Transition

> 부드럽게 처리하자~
>
> 변형의 중간 과정을 추가해준다고 생각하자!



- transition: **수치로 표현되는 값**이 변할 때 중간 과정을 추가한다.
  - s : 몇 초동안 처리한다!
    - transition-property: all; -> 모든 속성에 transition을 쓰겠다!
    - transition-duration: 1s; -> 재생 시간
    - transition-timing-function: ease; ->  가속도를 주어 더욱 부드럽고 자연스럽게
      - linear: 등속
      - chrome 개발자 도구를 이용하여 원하는 정도로 만들 수 있다.
    - transition-delay: 0s -> 동작 시작을 몇 초 뒤에 시작한다.
- width, height와 같은 값이 auto로 지정되어 있다면 transition이 먹지 않는다!
  - 수치가 아니니까 !!!!






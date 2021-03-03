# Animation



## keyframe

> 변화가 있는 지점



- `@keyframes [name]`

  - %로 지점을 지정한다.

    ```css
    @keyframes sample-ani {
        0% {
            transform: translate(0, 0);
        }
        50% {
            transform: translate(500px, 0);
        }
        100% {
            transform: translate(700px, 500px);
        }
    }
    ```



## css selector

- 해당 선택자의 style에 `animation: [name] 등등..;` 추가한다.

  - animation-name
  - animation-duration
  - animation-timing-function
  - animation-delay
  - animation-iteration-count
  - animation-direction
    - alternate: 왔다~ 갔다~
    - reverse: 반대로
    - alternate-reverse: 반대로 왔다~ 갔다~
  - animation-fill-mode
    - forwards: 마지막 상황에서 그대로 끝!
  - animation-play-state

  ```css
  .box {
      animation: sample-ani 2s linear infinite;
     	/*이름, 주기, 가속 반복*/
  }
  ```

  

## background image animation

> frame by frame animation


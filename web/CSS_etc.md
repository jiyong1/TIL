# CSS etc



## background-image



- `none` -> `url(' ')`



## background-repeat: 

> 반복 여부

- default : `repeat`
- `no-repeat` : 반복 없음
- `repeat-x`
- `repeat-y`



## background-position

> 기준을 잡는다.

- default : `0% 0%`;
- 방향 
  - `center` 
  - `top`
  - `bottom`
  - `right`
  - `left`



## background-size

> 배경 이미지 크기 속성

- default : `auto` (원래 이미지 그대로)
- `cover` : 긴 너비에 크기를 맞춤
  - 빈 공간은 생기지 않으나, **이미지가 잘릴 수 있다.**
- `contain` :  짧은 너비에 크기를 맞춤.
  - 이미지가 잘리지 않으나, **빈 공간은 생길 수 있다.**
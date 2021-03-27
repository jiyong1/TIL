# Scroll event

## Event

- `window.addEventListner('scroll', function_name);`



## scroll 내린 정도 확인

- `window.pageYOffset;`



## Object의 위치 잡기

- `object.offsetTop;`
  - 처음 위치만 가져온다.
- `object.getBoundingClientRect();`
  - 객체의 여러가지 속성을 담은 객체
  - object.getBoundingClientRect()`.top;` 을 통해 변화된 y좌표를 얻어낸다.
- `window.innerHeight;`
  - viewpoint의 높이
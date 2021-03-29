# Timing



## setTimeout(func, msec)

> 몇 초후에 함수를 실행!



- 초는 밀리초 단위로 지정한 초 후에 지정한 함수를 실행한다.
- 객체를 return한다!



## clearTimeout()

> 타임아웃을 지정해둔 것을 없앤다.



- setTimeout함수를 통해 얻은 객체를 인자로 넣어준다.



## setInterval(func, msec)

> 몇 초마다 함수를 실행



- 초는 밀리초 단위로 지정한 초 마다 지정한 함수를 실행한다.
- 객체를 return한다.



## clearInterval()

> 인터벌로 지정된 함수 실행을 멈춘다.



- `setInterval`함수를 통해 얻은 객체를 인자로 넣어준다.



## requestAnimationFrame()

> 초당 60번을 목표로 반복한다.

- `setInterval` 보다 많이 사용된다.

- 200번 반복하고 종료 예시

```javascript
function sample() {
    n++
    if (n>=200){
        return;
    }
    requestAnimationFrame(sample);
}
```





## cancelAnimationFrame()


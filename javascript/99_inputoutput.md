# [JS] 자바스크립트 입출력

> 코딩테스트 대비

**프로그래머스**등과 같은 경우는 함수 내에 문제풀이를 위한 데이터가 매개변수로 제공되기 때문에 문제가 되지 않지만 다른 경우 직접 데이터를 입력받아 문제를 풀이해야한다..

원래 `python`이나.. `C++`로 코딩테스트 대비를 했었는데.. FE 개발자가 되고 싶다라는 마음을 가지고 JavaScript 공부를 하다보니 JavaScript로 알고리즘 문제풀이를 진행할 때, 어떻게 파일을 입출력할지가 궁금해져서 몇군데 찾아보며 직접 작성해보았다!

<br>

## readline

```javascript
const readline = require('readline');
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

rl.on('line', function (line) {
  console.log(line);
  rl.close();
}).on('close', function () {
  process.exit();
});
```

검색을 통해 알아보다가 위와 같이 입력받는 것을 알게 되었다. 일단 대충 이해해보기론 **enter**가 되는 시점을 기준으로 한 줄로 평가하여 한줄 한줄 받아와서 콜백함수에서 사용자가 원하는 방식으로 수정하여 사용하고 문제를 풀이하는 것 같다. 이후, `rl.close`를 호출하여 프로세스를 종료시키는 것 같다.

그렇다면.. 실제 문제에서 많이나오는 2차원 배열 문제를 어떻게 저장하면 좋을까..?

직접 부딪혀보면서 코딩해보았다. 물론 정답이라 할 순 없다..

```javascript
const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout,
})

function solution(T, N, info){
    console.log(T);
    console.log(N);
    console.log(info);
    console.log(typeof info[0][0]);
}

let T = null;
let N = null;
let info = [];
let countT = 0;
let countN = 0;

rl.on('line', function(line){
    if (!T) {
        T = +line;
    } else if (!N) {
        N = +line;
    } else {
        info.push(line.split(' ').map(el => parseInt(el)));
        countN ++;
        if (countN === N) {
            countT ++;
            solution(T, N, info);
            N = 0;
            info = [];
        }

    }

    if (countT === T) {
        rl.close();
    }
}).on('close', function() {
    process.exit();
});
```

콜백함수 내에서 원하는 형식으로 데이터를 저장하는 로직을 구현하였다. 

- T를 null로 초기화 했기 때문에 처음 line을 읽어 들였을 때, T는 `false`일 것이고, T를 받아들일 수 있을 것이다.
  - +line을 하면 NUMBER타입이 된다.
- 그 다음은 당연히 배열의 크기인 N이 나올 것이다.
- 여기가 조금 이해하기 어려울 수 있는데.. 정사각 배열이라고 했을 때, 배열의 크기만큼(N) line을 받아오기 위해서 `countN`을 선언하여 **지금 몇번째 line을 input했는지 확인한다.** 그리고 원하는 line의 갯수만큼 input했을 때, `countT`를 올려서 TestCase 한개가 또 마무리되었음을 표시한다.
- 다음 TestCase가 남아있다면 N과 이차원 배열이 담긴 변수 info를 초기화 한다.
- TestCase를 전부 다 읽어들였다면(`countT === T`) 프로세스를 종료시킨다.

<br>

## fs

```javascript
const fs = require('fs');
let input = fs.readFileSync('/dev/stdin').toString().split('\n');

console.log(input);
```

백준에서는 위와 같이 fs를 사용하는 것을 권장한다고 한다. (readline은 느리다고..)

이렇게 읽어드리면 한줄 한줄 읽지 않고 input내에 모든 input의 정보가 담겨 들어오니.. 그냥 간편하게 데이터 형식을 저장해서 문제를 풀면 된다!
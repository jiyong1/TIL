## flow control

- receive buff에 남은 공간을 `receive window`라 한다.
  - 상대 send buff는 receive buff에 의존적이다.
- TCP segment header에 `receive window`에 대한 정보를 보낸다.

<br>

### dead lock 상황

- rcv window가 0bytes 인 상황에서 상대 send buff에 데이터가 없다면 rcv buff의 여유공간이 생겼다고 하더라도 send buff 입장에서는 알아차릴 수 없을 것이다. `dead lock`
- 이를 해결하기 위해 send buff에서는 **아주 조그마한 segment**를 주기적으로 보낸다.
  - header - 40bytes
  - data - 1bytes

<br>

### segment의 크기는 어떻게 결정할까?

> segment의 크기가 클수록 오버헤드의 비율이 줄어드니까 당연히 좋다.
>
> 그러나 app에서 write가 매우 천천히 일어나면 그만큼 기다려야 하므로 비효율적이다.

<br>

매우 직관적인 방법으로 문제를 해결한다.

- 일단 첫번째 segment는 데이터 크기가 어떻든 보낸다.
- feedback이 도착전에 Maximum을 넘어서는 데이터가 쌓인다면 보낸다.
- maximum이 되기전에 feedback이 온다면 쌓여있는 만큼 segment를 보낸다.

<br>

### 좀 더 효율적인 것

- receive window size가 어느정도 작으면 그냥 0이라고 보낸다.
  - 1byte 남았다고 1byte를 send쪽에서 보내는 게 비효율적..
  - 어느정도의 기준은 maximum segment size라고 한다.
- rcv buff데이터를 받자마자 ACK을 보내지 말고 잠깐만 기다렸다가 보낸다.
  - 받자마자 ACK를 보내는 것도 비효율적..
  - 좀만 기다려보면 금방 다른 데이터들도 올 수 있기 때문에
  - 좀만의 기준은 500ms라고 한다.. (~~실험적으로 얻어낸 값이라고 한다..~~)

<br>

## 3-way handshake

<br>

- 2-way handshake가 아닌 이유
  - 서버 측 입장에서 자신들이 보낸 응답에 대한 수신이 양호한지에 대해 들을 수가 없다.



1. `client `: TCP SYN msg (대화를 시작하자..)
   - data 없이 header 부분만 채워서 간다.
   - SYN flag = 1 / seq#X
2. `server` : SYN ACK (알겠어!)
   - SYN, ACK flag = 1 / ACK#X+1, seq#y
3. `clinet` : ACK (수신 양호..)
   - ACK flag = 1 / ACK#y+1
   - 여기서부터 데이터를 보낼 수 있다. (`http request`)



## Socket close

1. client app에서 `close call`
2. `client` : FIN flag = 1 / seq#x
3. `server` : ACK flag = 1 / ACK#x+1
4. `server` : FIN flag = 1 / seq#y
5. `client` : ACK flag = 1 / ACK#y+1
   - 여기서 주의할 점은 ACK를 보냈다고 해서 바로 끝내는 것이 아니라 조금 기다렸다가 끝낸다.
   - 혹시 ACK가 유실되어서 server측에서 계속 FIN을 보낼 수 있기 때문에!
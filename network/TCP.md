# TCP

<br>

## TCP overview

- point to point
- **reliable, in-order byte steam**
  - 에러없이 유실되지 않고 전송된다.
  - 전송 순서를 지켜가면서..
- pipelined
  - 한꺼번에 메시지가 많이 간다.
- full duplex data
  - 양쪽이 sender이자 receiver
- connection-oriented
- **flow controlled**
  - TCP의 segment가 나가는 속도는 상대방의 상태 혹은 네트워크 상황 등에 맞게 정해진다.



<br>

## TCP segment structure

<br>

![](TCP.assets/tcpSegment.jpg)

<br>

## TCP sequence number

- byte stream

<br>

## TCP acknowledgements

- 나는 몇번까지 완벽하게 받았고 몇번 seq를 기다린다.
  - ex) ACK#100
    - 99번까지 완벽하게 받았고 100 seq 기다리고 있다!
- cumulative ACK

<br>

## TCP round trip time, timeout

- 지정된 시간 안에 받았다는 응답이 오지 않으면 다시 segment를 보낸다.
- RTT를 매번 segment를 보내고 받을때마다 측정한다.
  - SAMPLE RTT
  - **재전송한 segment는 sample rtt에 포함하지 않는다.**
- `Estimated RTT = (1-a) * EstimatedRTT + a * Sample RTT` (a는 가중치)
  - 일반적으로 `a = 0.125`
- `TimeoutInterval = Estimated RTT + 4*DevRTT(safety margin)`



## Buffer와 동작 과정

각 소켓을 책임지는 TCP에 `send buff`, `receive buff`가 있다.

<br>

application이 socket으로 전송하는 속도와 TCP에서 전송하는 속도가 다르기 때문에 그 차이를 처리해야한다. 그래서 `send buff` 가 존재한다.

<br>

1. `send buff`에 존재하는 데이터를 하나 보내고 ACK을 기다리는 비효율적인 방법이 아니라 **한꺼번에 여러개의 데이터를 쏟아버린다.** 그렇다고 buffer에 존재하는 모든 데이터를 보내는 것이 아니라 한꺼번에 보내는 데이터의 양이 정해져 있다. (`window size`)
   - window size : 1000bytes
   - 각 200bytes인 데이터 5개 : seq#0, seq#200, seq#400, seq#600, seq#800
2. 상대에게 `ACK#..`를 받으면 해당 데이터를 send buff에서 지우고 `send base`와 `window`그리고 `timer` 를 이동시킨다. ( `send buff`는 혹시라도 재전송해야하는 상황이 생길 것을 대비해 ACK를 받지 않은 데이터를 보관한다.  )
   - `ACK#200` 을 받았다.
   - send buff에서 seq#0을 제거하고 send base를 변경한다.
   - window의 위치가 변경되었으니 버퍼에 존재하는 다른 데이터를 전송한다. ( `seq#1000` )
3. 위와 같은 과정을 진행 중에 데이터 하나가 유실되어 하나를 건너띄어 받았다면 이전과 같은 ACK 를 보낸다. 받은 데이터를 위로 올려보내지 않는다. ( `receive buff` 는 `in-order delivery`를 위한 장치 )
   - `seq#200`을 받지 않고 `seq#400` 부터 데이터를 받았다.
   - 나는 `seq#200`을 기다린다는 의미로 똑같이 `ACK#200` 을 보낸다.
   - 타임아웃이 일어나 다시 `seq#200` 을 다시 보낸다.
   - 올바르게 받았다면 `ACK#1200` 을 보내고 receive buff에 쌓여있는 데이터를 올려보낸다.

<br>

**실제로는 receive buff ack와 send buff seq가 묶여서 같이 간다.**



<br>



## TCP fast retransmit

> 타임아웃이 생각보다 많이 여유로운데.. send buff 입장에서 더 빠르게 유실을 판단하여 재전송하는 방법이 없을까..?

<br>

이전에 받은 ACK와 동일한 ACK를 3번 더 받았을 경우 유실됐다고 판단하여 데이터를 다시 보낸다..

- 실험적으로 3번이 적당하다고 한다..



<br>



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

![](TCP.assets/3wayHandshake.jpg)

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

<br>

## TCP congestion control

> 네트워크 혼잡 상황에 맞춰서 보내는 데이터 양을 결정한다.
>
> flow control과는 다르다.

<br>

### congestion 시나리오

- 하나의 라우터, 유한한 크기를 갖는 buffer
- 이상적으로 라우터의 buffer가 빈 공간이 있는지 알고 있다고 가정한다면 빈 공간이 존재할 때만 보내면 되니까 packet loss는 없을 것이다.
- 그러나 현실적으로 빈 공간이 존재하는지 알 수 없기 때문에 packet loss가 일어날 수 밖에 없다.
  - 재전송을 하게 된다.
- 또한, packet loss가 일어나지 않았더라도 time out이 일어나 재전송이 일어날 수 있다.
- `많이 보내서 네트워크가 막힌건데.. 네트워크가 막혀서 더 많이 보내게 된다..`

<br>

### congestion 시나리오 2

- 여러개의 라우터
- `upstream router` 부터 `downstream router`까지 단계 단계 거쳐가다 경쟁에서 이기지 못하고 packet loss가 일어난다.
- 결국 이제까지 network resource를 사용한 것이 도루묵..

<br>

`조금의 손해를 보더라도 모두가 보내는 속도를 조절하면 잘 사용할 수 있다. 그 속도를 찾아보자..`

그러기 위해서는 네트워크 상황을 인지하여야 한다.

- `feedback` 을 근거로 네트워크 상황을 판단한다.

<br>

### additive increase / multiplicative decrease

> send buff는 rcv buffer의 window size와 router의 buffer의 크기 중 최솟값을 window 사이즈로 한다.

<br>

- segment를 보내고 그에 대한 응답이 제대로 잘 들어온다면 `MSS(Maximum Segment Size)` 만큼  늘린다!
  - **네트워크 상황이 좋다고 판단**하는 것
- 피드백이 안오는 순간, 잘못됐다는 판단을 하고 **window size를 절반**으로 줄인다.
- `조심스럽게 늘리고 팍 줄인다!`
- 처음에는 매우 조심스럽게 접근한다. - `slow start phase`
  - 1 MSS만 보내서 시작한다!
  - 처음에 증가할 때는 배수로 증가한다! (`slow start threshold`를 지정하여 그 값을 넘어서면 linear하게 증가한다.)
    - linear하게 증가하는 구간을 `Congestion Avoidance phase` 라고 불린다.
  - 그러므로 금방 어느 수준에 도달할 수 있다.

<br>

![tcpCongestionControl](TCP.assets/tcpCongestionControl.png)

[그림 출처](https://www.researchgate.net/figure/TCP-congestion-control-algorithms-The-congestion-window-size-depends-on-the-congestion_fig2_228825379)

<br>

### loss 종류에 따라 다른 대처

> timer expired
>
> 3 duplicate ACK

직관적으로 `timer expired`로 인한 loss가 일어났을 때가 `3 duplicate ACK (3번의 중복된 ACK)` 가 일어났을 때에 비하여 네트워크 상황이 안좋다는 것을 알 수 있다.

<br>

최초의 TCP에서는 어떤 종류의 loss가 일어나든지 간에 매우 겸손한 자세로 **congestion window size를 1 MSS로 변경하고 threshold 값을 timeout이 일어나기 전의 1/2로 줄인 후**, `slow start`를 시작한다.

<br>

두번째 TCP버전에서는 timer expired가 일어났을 때는 똑같이 동작을 하고,  `3 duplicate ACK`로 인한 loss라면 **congestion window size와 threshold 값을 현재 값의 1/2로 줄이고** `linear increase`를 시작한다.

<br>

---

<br>

## TCP throughput

> TCP 속도
>
> TCP를 사용했을 때 네트워크 속도는 네트워크가 결정한다.

- `avg TCP throughput = 3/4 * (W/RTT)` bytes/sec
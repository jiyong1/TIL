# [네트워크] Link layer

> 두개 이상의 packet이 나올 경우 전달이 제대로 되지 않는다.
>
> 이러한 충돌을 어떻게 해결할 것인가?

app layer (message) -> transfer layer (segment) -> network layer (packet) -> `link layer (frame)`

<br>

## Multiple access links, protocols (MAC)

<br>

### TDMA (time division multiple access)

> channel partitioning
>
> 이동통신 lte, 3g에서 사용한다.

- 정해진 시간에만 말한다.
- 충돌은 일어나지 않을 것이다.
- 근데 한명만 이야기 하고 있으면..? - `단점`

<br>

### FDMA (frequency division multiple access)

> channel partitioning
>
> 이동통신 lte, 3g에서 사용한다.

- 주파수를 나누어서 하는 것
- 서로 다른 주파수 사용하니까 충돌은 일어나지 않을 것
- 마찬가지로 낭비가 일어날 수 있다.

<br>

### CSMA (carrier sense multiple access)

> random access
>
> ethernet이랑 wifi에서 사용한다.

- 누군가 이야기하는지 들어보고 조용하면 내가 이야기 한다.
- 말이 끝자나마자 말하려고 하면 collision이 발생할 수 있다.
- 물리적인 속도를 가지고 있기 때문에 propagation delay에 의해 충돌이 일어날 수 있다.

<br>

#### CSMA/CD (collision detection)

> 말이 겹치면 데이터 전송을 멈춘다.

- 말이 겹치게 되면 데이터를 다 전송하더라도 듣는 입장에서는 무슨 말인지 못알아듣기 때문에 시간이 낭비된다.
- 이러한 낭비를 줄이고자 해서 collision이 감지되면 데이터 전송을 멈춘다.
- 랜덤 타임을 돌리고 끝나면 다시 재전송 시도 (반복)
  - 랜덤 타임의 범위가 좁으면 빠르게 재전송할 수 있지만 또 충돌이 날 가능성이 있다.
  - 첫 충돌에 대해서는 빠른 시간 내에 재전송하기 위해 랜덤 타임 범위가 좁다.
  - 또 충돌이 발생하면 다음 충돌부터는 랜덤 타임 범위가 넓어진다.
  - 그러니 인터넷을 사용하는 사람이 많아질수록 느리다는 느낌을 받는 것!

<br>

사용자가 많으면 **TDMA, FDMA** 가 효율적, 사용자가 적으면 **CSMA**가 효율적

link layer에서는 `feedback (ACK)`이 없기 때문에 collision detect가 100%로 일어나야한다.

<br>

### Taking turns Mac protocols

토큰이 있는 host가 데이터를 전송한다.

토큰 잃어버리면 큰일난다.. 잘 사용하지 않는다고 함

<br>

## Ethernet: physical topology

> 유선 상황

<br>

### Ethernet frame structure

- `header`
  - preamble - ethernet frame 이다
  - destination address : `MAC address`
  - source address : `MAC address`
  - type
- `data`
  - IP packet
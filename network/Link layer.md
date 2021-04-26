# [네트워크] Link layer

> 두개 이상의 packet이 나올 경우 전달이 제대로 되지 않는다.
>
> 이러한 충돌을 어떻게 해결할 것인가?

app layer (message) -> transfer layer (segment) -> network layer (packet) -> `link layer (frame)`

<br>

![](Link layer.assets/linklayer.jpg)

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

#### 충돌이 일어났는데 충돌 탐지를 하지 못하는 경우

- A에서 frame을 전송한다. (아주 작은 frame)
- frame을 다 전송하자마자 다른 곳에서 충돌되는 frame을 보냈다.

이러한 경우를 방지하기 위해서 `propagation delay`에 연관지어 `Minimum frame`사이즈 지정해놓았고,  Minimum frame 사이즈 이상의 frame을 보내야한다.

만약 minimum보다 작은 사이즈만 보내는 경우라면 `padding`을 넣어서 보낸다.

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
  - destination address : `MAC address` (48 bits)
  - source address : `MAC address` (48 bits)
  - type
- `data`
  - IP packet

<br>

## MAC address

> IP 주소는 위치에 종속되어 계속 바뀔 수 있지만
>
> MAC 주소는 unique 하다.

- 앞 24bit : 제조사
- 뒤 24bit : 제품 번호

<br>

## ARP (address resolution protocol)

> IP주소를 가지고 MAC 주소를 얻어온다.

최초에 DHCP(Dynamic Host Configuration Protocol)을 통해서 GateWayRouter의 IP주소를 얻어오지만,  해당 interface의 MAC 주소는 알지 못한다. 이를 어떻게 해결할 것인가?

- 지금 1.1.1.1 IP 주소를 가지고 있는 분은 MAC 주소 좀 알려주세요~ (`broadcast`)
  - 위의 packet을 `ARP query` 라고 한다.
  - frame header type에 ARP query임을 명시한다.
    - 이외에도 IP packet, ARP response 등의 type이 존재한다.

<br>

- frame header
  - type : ARP query
  - src : 나의 MAC address
  - dst : FF-FF-FF-FF-FF-FF (broadcast)
- data
  - 1.1.1.1 주소를 가지고 있는 분 MAC 주소 좀 알려주세요.

<br>

이후 알게된 정보를 `ARP TABLE`에 정보를 남겨둔다. 이를 참조하여 다음 interface로 이동한다.

router와 router 사이에서도 forwarding table을 참조하여 dst IP address를 알아내고, dst IP address와 ARP TABLE을 통해 다음 interface의 MAC주소를 얻어내는 형식으로 최종 목적지까지 이동한다.

<br>

## Switch

> bus vs **star**
>
> broadcast domain을 분리한다.
>
> host 입장에서는 carrier sense를 했을 때 항상 조용하다.

- switch내에 switch table이 존재하여 어떤 interface에 host가 존재하는지 알고있다.
- switch table을 얻기 위해 `self-running`이 이루어진다.
  - frame을 받았을 때 frame의 source address를 보고 하나를 배운다.
  - destination address(MAC)을 모른다면 flood(주소 정보를 아는 interface 말고 모든 interface에 다 보낸다.)
- switch도 한정된 interface 개수만 호환하기 때문에 `계층화`를 시켜 연결한다.
- switch가 하는 일을 `switching` 이라고 한다.
- switch에게 MAC address는 없다.

<br>


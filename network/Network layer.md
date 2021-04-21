# [네트워크] Network layer

> 전송계층을 배웠으니 이제 뚜껑을 열어 Network 계층에 대해 알아보자.
>
> TCP segment가 IP packet으로 들어온다.

<br>

## 네트워크 계층의 주요한 기능

1. `forwarding`
   - input interface로 packet이 들어오면 그 packet이 가고자하는 목적지에 따라서 알맞은 interface로 forwarding 해주어야 한다.
   - router안에 `forwarding table`을 참조하여 보낸다.
   - forwarding table은 어떻게.. 채워져있지..?
2. `routing`
   - forwarding table을 채우는 것을 routing이라고 한다.

<br>

## forwarding table

forwarding table entry에 목적지의 주소가 모두 담겨있게 되면 table의 크기가 너무 커진다.

주소 자체가 들어가는 것이 아니라 **주소 range**가 들어간다.

![](Network layer.assets/forwardingTable.jpg)

- 별 표시를 통해 범위를 지정한 것이다.
- `longest prefix matching`
  - 여러개 entry와 매칭이 되었을 때, **가장 길게 매칭되는 곳으로 forwarding !!**
  - ex) 광주광역시, 광주광역시 서구..
  - 광주광역시 서구라고 한다면 당연히 광주광역시 서구의 interface로 가야지..

<br>



## Router architecture overview

![](Network layer.assets/routerArchitecture.jpg)

- forwarding table을 `routing processor`가 만들어 준다.
- 만들어진 forwarding table은 각 **input port에 독립적으로 저장된다.**
  - 병렬적으로 처리하여 속도를 빠르게 하기 위해서
- 아무리 연산속도가 빨라도 packet이 들어오는 속도가 더 빠를 수 있기 때문에 각 input port에 queue가 존재한다.
- output port에도 몰릴 수 있기 때문에 queue가 존재한다.

<br>

## IP packet의 형태

![](Network layer.assets/packet.jpg)

- `TTL (Time To Live)` : 최초의 숫자를 시작으로 router에서 forwarding 할 때 1씩 감소시킨다.
  - 영원히 packet이 살아있는 것을 방지하기 위해서
- `Upper layer` : TCP, UDP 등 상위 layer 어디로 올려보내야 되는지..
- `source IP address` 와 `destination IP address`가 중요하다.

<br>

## IP Address (IPv4)

- IP는 특정 host를 지칭하는 것이 아니다!
- **IP 주소란 interface를 지칭하는 것이다.**

<br>

### Scalability Challenge

- host들이 각자 IP주소를 배정받아 가지고 있다고 가정해보자.
- 이렇게 되면 사용자가 많아질 때 forwarding table entry 개수가 무지하게 많아진다.
- 결과적으로 matching의 속도가 느려지게 된다.

<br>

### Hierarchical Addressing

> 스케일이 커지면 무조건 계층화
>
> IP 주소 역시 계층화가 되어있다.



- 앞 24bits : Network id (`==prefix==subnet`) - 사실 가변적이다.
- 뒤 8bits: Host
- `Subnet Mask` : 어디까지 Network id(prefix)인지 machine이 이해할 수 있도록 존재한다.
  - bitwise AND
- 근데 이렇게 되면 256개의 host만 network 통신이 가능한가..?

<br>

###  가변적인 prefix 크기

> Classless Inter-Domain Routing (CIDR)

각 기관의 size에 맞게 유연하게 prefix 크기를 정한다.

<br>

### Subnets

- router를 거치지 않고 접근할 수 있는 interface들의 집합
- router의 interface들은 각자 다른 subnet

<br>

## IPv6

주소 공간이 128bits

아직까지 IPv4를 사용하고 있다. 못갈아타는데는 이유가 있다..

- 기존에 사용하고 있던 IPv4 라우터 장비를 교체해야 한다.
- 기존의 IPv4 생태계를 뒤집기는 힘들다..
- 근데 진짜 문제가 된다면 무슨 수를 써서라도 바꿔야하는데 바꾸지 않아도 문제가 되지 않는다

<br>

## Network Address Translation (NAT)

- IP 주소는 실질적으로 unique 해야한다.
- **내부적으로만 유일한 주소를 사용자에게 배정한다.**
- source 에서 나가거나 들어올 때 IP를 변경한다.



![](Network layer.assets/nat.jpg)

- **다시 서버측에서 들어올 때 port번호를 가지고 누구인지 판단할 것이다.**
- 사실은 host를 구분하기 위해서 IP 주소를 사용해야하는데 port번호를 사용하고 있다.



<br>

## Dynamic Host Configuration Protocol (DHCP)

> 애플리케이션 계층의 이야기



- DHCP server가 존재한다.
- DHCP서버에게 IP주소를 요청하고, IP주소를 임대받는다.
- 임대 절차
  1. DHCP Discover (클라이언트 -> DHCP 서버 / 브로드캐스트 메시지)
     - 단말이 DHCP 서버를 찾기 위한 메시지
     - 혹시 DHCP 서버 있나요?
  2. DHCP Offer (서버 -> 클라이언트)
     - 단순히 서버의 존재만을 알리지 않고, 클라이언트에 할당할 IP 주소 정보를 포함한 다양한 정보를 실어서 클라이언트에게 전달한다.
     - 저 여기있어요.. 그리고...
  3. DHCP Request (클라이언트 -> 서버)
     - 클라이언트가 사용할 네트워크 정보를 요청
  4. DHCP ACK (서버 -> 클라이언트)



<br>

## IP fragmentation, reassembly

router들 사이의 link에서 지원할 수 있는 최대 packet 크기가 다르다.

link에서 지원할 수 있는 최대의 packet 사이즈를 `MTU (Maximum Transmission Unit)` 라고 한다.

따라서 packet사이즈가 MTU보다 크게 되면 못지나가게 되는데 데이터를 버리는 것은 너무 아까우니 데이터를 쪼갠다. ( **fragmentation** )

결국 도착점에 도착했을 때 다시 조립(assemble)을 해야하는데 assemble하기 위한 기록을 packet에 해놓는다. - `fragflag, 16-bit identifier, offset, length`



### fragmentation example

> 4000 byte의 데이터
>
> MTU = 1500 bytes



1. header : 20bytes / data : 1480bytes - `length : 1500`
   - `fragflag` : 1 (저 .. 뒤에 동생이 있습니다.)
   - `offset` : 0 (원래 데이터에서 0번부터 시작했습니다)
2. header : 20bytes / data : 1480bytes - `length : 1500`
   - `fragflag` : 1 (저 .. 뒤에 동생이 있습니다.)
   - `offset` : 185 (1480/8) - header의 3bit를 줄이고자..
3. header : 20bytes / data : 1020bytes - `length : 1040`
   - `fragflag` : 1 (제가 마지막입니다.)
   - `offset` : 370 (2960/8)


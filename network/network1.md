# 어플리케이션 계층

> 프로세스 대 프로세스의 관점

- server
  - always-on host
  - permanent IP address
  - data centers for scaling
- clients
  - communicate with server
  - may be intermittently connected
  - may have dynamic IP addresses
  - do not communicate directly with each other

- socket
  - 운영체제가 제공하는 system call 중 하나
  - socket이라는 interface를 통해서 process간의 통신이 가능하다.
  - IP address를 통해서 머신에 접근, Port 번호로 process에 접근



## Internet transport protocols services

> TCP, UDP



- TCP service
  - reliable transport
  - flow control
  - congestion control
  - does not provide
  - connection-orientied
  - email, remote terminal access, Web, file transfer
- UDP service
  - unreliable data transfer
  - does not provide




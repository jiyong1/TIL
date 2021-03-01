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



## Web and HTTP



### HTTP : Hypertext transfer protocol

- Web's application layer protocol
- client/server model
- request / response
- uses TCP
- HTTP is stateless



#### Non-persistent HTTP

RTT : time for a small packet to travel from client to server and back

- HTTP response time
  - one RTT to initiate TCP connection
  - one RTT for HTTP request and first few bytes of HTTP response to return
  - file transmission time
  - non-persistent HTTP response time = 2RTT + file transmission time



#### Persistent HTTP

> 훨씬 효율적

- non-persistent HTTP issues
  - requires 2 RTTs per object
  - OS overhead for each TCP connection
  - browsers often open parallel TCP connections to fetch referenced objects
- propagation delay에서 이득을 볼 수 있다



#### HTTP request message

- two types of HTTP messages : request, response
- HTTP request message
  - ASCII (human-readabel format)
  - request line
    - 무슨 파일을 요청합니다
  - header lines
    - 부가적인 정보
  - carriage return, line feed at start of line indicates end of header lines



#### HTTP response message

- HTTP response message
  - 부가적인 정보 + data
  - status line (protocol / status code / status phrase)
    - 자, 여기 올바르게 전달한다!
  - header line
    - set-cookie 등등
  - data, data, data, data...



#### User-server state : cookies

> stateless를 보완하기 위해 나온 것

- 이름이 왜 쿠키야? - 쿠키를 쪼개서 둘이 나눠가지고 맞추어본다.



#### Web caches (proxy server)

> 현재의 Web browsing structure는 중간에 한 녀석이 껴있다.

- goal : satisfy client request without involving origin


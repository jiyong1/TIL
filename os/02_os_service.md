# [운영체제] 운영체제 서비스

<br>

## 1. 프로세스 관리

**프로세스**는 실제 메인 메모리에서 실행 중인 프로그램을 말한다. **프로그램**은 하드디스크와 같은 보조기억장치에서 동작 하지 않는 상태이다.

프로세스 관리의 주요 기능은 다음과 같다.

- 프로세스의 생성과 소멸
- 프로세스 활동 일시 중지, 활동 재개
- 프로세스간 통신
- 프로세스간 동기화
- 교착 상태 관리

<br>

## 2. 메인 메모리 관리

메인 메모리는 프로그램이 실행되기 위한 공간이다. CPU는 메인 메모리에 있는 프로세스와 소통할 수 있다. 메인 메모리 관리는 메인 메모리를 효율적으로 사용하도록 관리한다.

- 프로세스에게 메모리 공간 할당
- 메모리의 어느 부분이 어느 프로세스에게 할당되었는가 추적 및 감시
- 프로세스 종료 시 메모리 회수
- 메모리의 효과적 사용
- 가상 메모리: 물리적인 실제 메모리보다 큰 용량을 사용할 수 있다.

<br>

## 3. 파일 관리

디스크는 물리적으로 Track과 Sector로 구성되어 있다. 이를 사용하기 쉽게 하기 위해서 파일이라는 논리적인 데이터를 관리하고 사용한다.

사실 우리가 사용하는 파일은 복잡하게 하드디스크와 같은 기억 장치에 저장되어 있는데 이를 좀 더 편리하게 사용할 수 있도록 **파일**이라는 논리적인 형태로 운영체제에서 관리한다.

- 파일의 생성과 삭제
- 폴더의 생성과 삭제
- 기본 동작 지원 : open, close, read, write, create, delete
- 물리적 형태 Track, Sector - 논리적 형태 파일 간의 매핑(mapping)
- 백업

<br>

## 4. 보조기억장치 관리

하드 디스크와 같은 보조기억장치를 관리한다.

- 빈 공간 관리
- 저장공간 할당
- 디스크 스케줄링

<br>

## 5. 입출력 장치 관리

키보드, 마우스, 스피커, 마이크, 프린터 등의 입출력 장치를 관리한다.

- 장치 드라이브
- 입출력 장치 성능 향상: buffering, caching, spooling

<br>

## 6. 시스템 콜

시스템 콜은 프로세스에서 운영체제 서비스를 필요로 할 때 사용하는 호출이다.

프로세스의 동작 중 운영체제 서비스가 필요하면 **시스템 콜**을 통해 운영체제 안의 해당 코드로 점프할 수 있다.

- `Process`: end(정상적인 종료), abort(강제 종료), load, execute, create, terminate, get/set attributes, wait event, siganl event
- `Memory`: allocate, free
- `File`: create, delete, read, write, open, close, get/set attributes
- `Device`: request, release, read, write, get/set attributes, attach/detach devices
- `information`: get/set time, get/set system data
- `communication`: socket, send, receive




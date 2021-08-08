# IAM

<br>

## IAM 계정

### ROOT account MFA

> Multi Factor Authentiacation

- Root 계정의 보안이 취약하기에 설정한다.

- 실제 사용하는 계정은 아니고 **IAM** 개발자 계정을 만들어서 사용한다 !
- 핸드폰 바꾸면 MFA 해지하자..

<br>

### IAM admin

- 권한 자체는 Root account와 거의 동일하다.
- 루트 계정이 노출되면 admin 계정으로 손쉽게 제어할 수 있다.

<br>

1. 그룹 생성하기
2. `AdministratorAccess` 정책을 그룹에 선택
3. 그룹에 사용자 추가
   - 사용자 이름
   - 액세스 유형 선택
   - 자동 비밀번호가 안전하다.
   - Csv 파일 다운로드 받아 비밀번호를 받아 볼 수 있다.

<br>

### 개발자 계정

1. 그룹 생성
2. `PowerUserAccess` 정책을 선택한다.
   - 모든 리소스를 사용할 수 있으나, 계정 정보에는 접근할 수 없다!
   - 자기 자신에 대한 정보를 변경하거나 할 순 있다.

<br>

---

<br>

## IAM Policy

- JSON 포맷의 문서

- `Authentication(인증)` : 본인임을 검증한다.
- `Authorization(권한 부여)` : 권한이 부여 되어있는지를 확인한다.

- AWS 에서...
  - 인증의 주체는 user
  - IAM Policy는 권한 부여의 주체

<br>

### IAM Group

- 공통의 권한을 가지는 사용자의 집합
- 그룹을 생성 후 IAM Policy를 연결
- 그룹에 사용자 추가
- 그룹 내 사용자는 **그룹과 연결된 Policy의 권한을 부여받음**

<br>

### IAM User

- 사용자에게 직접 Policy를 추가할 수 있음
- 인증 방식과 사용 용도
  - ID / PW : 관리 콘솔에서 사용
  - AccessKey ID / Secret access Key : CLI, SDK, Web API에서 사용
- Long term credential 이라고 함
  - Short term = Role

<br>

### IAM Policy의 종류

- AWS 관리 정책
  - AWS가 미리 만들어 놓은 정책
- 사용자 관리 정책
  - 사용자가 직접 생성한 정책
  - 기존 정책으로부터 생성 및 수정 또는 직접 생성 가능

<br>

---

<br>

## IAM Role

> 특정 개체에게 리소스의 접근 권한을 부여하기 위해 사용
>
> Short term credential

- 주로 AWS 서비스들이 직접 다른 AWS 서비스를 제어하기 위해 사용한다.
- 사용자나 응용 프로그램에서 일시적으로 AWS 리소스에 접근 권한을 얻을 때도 사용

<br>

### IAM Role의 주요 구성요소

- Role ARN : 역할을 호출하기 위해 필요
- IAM Policy : 이 역할이 어떤 권한을 부여를 할 수 있는가
- 신뢰 관계 : 어떤 개체가 IAM Role을 호출할 수 있는가

<br>

### IAM Role 사용예제

- EC2 Role : EC2 인스턴스에게 AWS 서비스 접근권한을 부여
- Lambda Execution Role: 람다에서 S3로부터 파일을 읽고 싶을 때 role에 권한 지정
- 다른 계정의 사용자에게 내 계정의 Dynamo DB에 접근 권한 부여
- 안드로이드 앱이 S3로 직접 동영상을 업로드할 때 사용
  - 앱 -> 서버 -> S3
  - 앱 -> S3 : role

- 넷플릭스 등에서 일시적으로 영화에 접근하게..

<br>

### ARN

> Amazon Resource Name
>
> 아마존에서 리소스를 유일하게 식별할 수 있는 구분자

- `arn:partition:service:region:account-id:resource-id`
- `arn:partition:service:region:account-id:resource-type/resource-id`
- `...resource-type:resource-id`






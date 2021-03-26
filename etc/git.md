# Git

> Git은 분산 버전 관리 시스템(DVCS)이다.
>
> 소스코드의 이력을 추적 & 관리한다. 개인 프로젝트 뿐만 아니라 협업 단계에서도 활용된다.
>
> 협업과 버전관리



## 1. 준비

> 윈도우 기준

- 윈도우에서 git을 사용하기 위해서는 `git bash`를 설치한다.
- git을 활용하기 위해서는 GUI 툴인 `source tree`, `github desktop` 등을 활용할 수 있다.
- 초기 설치를 완료한 이후에 컴퓨터에 작성자(`author`) 정보를 등록한다.

```bash
# author 정보 등록
$ git config --global user.name {user name}
$ git config --global user.email {user email}

# author 정보 확인
$ git config --global --list
# 결과
user.email=jyong9591@gmail.com
user.name=Jiyong Kim
```



## 2. 로컬 저장소(Local Repository) 활용하기

### 2.1 저장소 초기화

```bash
$ git init
```

- `.git` 폴더가 생성되며, 이곳에 저장소의 git 관련된 모든 정보가 저장된다.
- git bash에 (`master`) 라고 표시된다. 이는 현재 `master`라는 branch에 있다는 뜻이다.



### 2.2 add

현재 작업 공간(working directory)에서 변경된 사항을 커밋으로 기록하기 위해서는 `staging area`를 거쳐야 한다.

```bash
$ git add . # 현재 디렉토리
$ git add images/ # 특정 폴더
$ git add iu.jpg # 특정 파일
```



### 2.3 commit

`commit`은 이력을 확정짓는 명령어다. 해당 시점의 스냅샷을 기록한다.

`commit` 시에는 반드시 메시지를 작성해야 하며, 메시지는 변경사항을 확인할 수 있도록 명확하게 작성한다.

```bash
$ git commit -m "I'm message"
```

`commit`이후에는 `log`명령어를 통해 지금까지 작성된 이력을 확인한다.

```bash
$ git log
$ git log --oneline # 압축된 버전
```



## 3. 원격 저장소(Remote Repository) 활용하기

> 원격 저장소 기능을 제공하는 서비스에는
>
> `Github`, `Gitlab` 등이 있다. 그 중에서 `Github`을 활용한다.

### 3.1 준비

- Github에 새로운 Repositary 생성



### 3.2 원격 저장소 등록

```bash
$ git remote add origin {github url} # origin은 바꾸어줘도 가능함
$ git remote add gitlab {gitlab url}
```

- 원격 저장소(`remote`)로 `origin`이라는 이름을 가진 `github url`을 등록(`add`)한다.
- 등록된 원격 저장소 목록을 보기 위해선 아래 명령어를 입력한다.

```bash
$ git remote -v
```



### 3.2 Push

```bash
$ git push origin master # origin -> gitlab
```

- `origin`이라는 이름으로 등록된 원격 저장소에 `master`브랜치를 업로드(`push`)
- 이후 변경 사항이 생길 때마다 `add` -> `commit` -> `push` 순으로 작업을 수행한다.



### 웹 IDE

웹에서 수정



## 역행



### restore



### reset

```bash
$ git reset ????
```

- commit history도 과거로 돌아간다.



### revert

```bash
$ git revert ????
```

- commit history는 그대로 남는다.
- 코드를 되돌릴 수 있다.
- 원격 저장소와 로컬 저장소의 충돌을 미연에 방지할 수 있다.



## branch



### branch 확인

```bash
$ git branch
```

- 관리하고 있는 `branch`의 목록을 볼 수 있다.



### branch 생성

```bash
$ git branch branch_name
```



### branch 이동

```bash
$ git switch branch_name
```

- branch를 변경하고 데이터를 변경 후 commit 하면 이전 branch에서는 반영이 되지 않는다.
- commit 기록, 실제 파일 모두 변경된다.



### branch 삭제

```bash
$ git branch -d branch_name
```



### pull

```bash
$ git pull origin branch_name
```



### merge

```bash
$ git merge branch_name
```

- 같은 파일을 수정했을 경우 충돌이 일어난다.
  - 적용할 파일을 선택하고 다시 add, commit
- branch가 할 일이 끝나면 지운다.



```bash
git log --oneline --graph
```

- 그래프로 commit 도식화
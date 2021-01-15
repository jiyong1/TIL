# Git

> (분산) 버전 관리 시스템 DVCS(Distributed Version Control System)
>

- 코드의 History 를 관리하는 도구로서 개발된 과정과 역사를 볼 수 있으며, 프로젝트의 이전 버전을 복원하고 변경 사항을 비교, 분석 및 병합도 가능하다.

- 사진을 여러 클라우드에 저장하듯, git또한 github, gitlab등에 저장한다.



## git 작업 흐름

- add : 커밋할 목록에 추가 (커밋        new file:   startcamp/day2/crawling.md 준비)
- commit : 커밋(create a snapshot) 만들기
- push : 현재까지의 역사 (commits) 가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

`git config --global user.email {email}`

`git config --global user.name {name}`

원하는 폴더로 이동 -> git bash here

`git init`

`git add . `모든 하위폴더 경로 추가

`git status`로 현재 무엇이 바뀌었는지 add되어있지 않거나 되어있지만 아직 commit 되어있지 않은 것을 확인할 수 있다.



내 폴더에 존재하는 Repositary는 local

github에 존재하는 것은 Remote Repositary

`git remote add origin {}`

`git push origin master` 
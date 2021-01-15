[toc]



# Crawling (크롤링)

> 웹은 요청과 응답으로 이루어진다.



네이버에 ssafy를 검색하면 다음과 같은 url이 생성된다.

https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=ssafy



https://search.naver.com/search.naver + `?` + `query=ssafy`로 검색해도 동일한 결과를 얻을 수 있다.



## HTML

> requests와 Beautifulsoup



### 1.1 requests

- requests.get('주소')
  - 주소에 요청 보내서, 정보 받아줘
- requests.get('주소').status_code
  - 주소에 요청 보내서, 정보 받아서, 상태만 뽑아줘
- requests.get('주소').text
  - 모든 정보를 스트링으로



```python
import requests

url = 'https://naver.com'
response = requests.get(url)
status = response.status_code # 200이면 정상!
txt = response.text # type = string
```



### 1.2 BeautifulSoup

> requests의 결과를 예쁘게 바꿔준다.



- BeautifulSoup(문서)

```python
import requests
from bs4 import BeautifulSoup

url = 'https://naver.com'
response = requests.get(url)
status = response.status_code # 200이면 정상!
txt = response.text # type = string

soup = BeautifulSoup(txt) # type = bs4.BeautifulSoup
```

- BeautifulSoup.select(경로)
  - 원하는 곳으로 찾아가게 해준다.



```python
# 코스피 지수
import requests
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
# print(response.status_code)
soup = BeautifulSoup(response, 'html.parser')
# html.parser 기입
result = soup.select_one("#KOSPI_now").text
# html내 아이디(id는 유일한 존재)

print(result)
```



- select와 select_one
  - html의 클래스 같은 경우는 여러가지가 올 수 있다. 이때, `select_one`을 사용하게 되면 문서 처음에 나오는 클래스로 받아온다.
  - `select`는 해당 클래스로 선언되어 있는 정보 모두 가져온다.



## API (Application Programming Interface)

> 응답 받을 때 HTML이 아닌 JSON이라는 형태로 받는다
>
> 서비스와 서비스가 소통하는 언어 수단? ex) 웹사이트 로그인 (카카오로 로그인)



- JSON (JavaScript Object Notation)
  - 데이터만을 주고 받기 위한 표기법
  - Python의 `Dictionary`와 `List` 구조로 쉽게 변환하여 활용할 수 있다.



### 예상나이 예제

```python
import requests

name = input()
url = f"https://api.agify.io/?name={name}"
response = requests.get(url).json() #json

print(f"{name}님의 예상 나이는 {response['age']}살 입니다.")
```



### 공공데이터

> 앞의 예제와는 다르게 굉장히 복잡하게 구성되어 있어 사용법을 제공한다.

- 문서를 확인하거나 참고한 사이트에서 미리보기를 통해 얻어보자
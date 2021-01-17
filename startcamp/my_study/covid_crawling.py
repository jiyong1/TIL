import requests
from bs4 import BeautifulSoup

url = "https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=%EC%BD%94%EB%A1%9C%EB%82%98"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
result = soup.select_one("#_cs_production_type > div > div:nth-child(7) > div.status_info > ul > li.info_01 > em").text

token = ""
api_url = f"https://api.telegram.org/bot{token}"
chat_id = ""
txt = f"금일 국내 코로나 확진자 수는 {result} 입니다."

send_url = f"{api_url}/sendMessage?chat_id={chat_id}&text={txt}"
requests.get(send_url)

# 3. 메시지 보낸 사용자의 아이디 값 찾기

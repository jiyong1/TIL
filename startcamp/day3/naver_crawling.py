import requests
from bs4 import BeautifulSoup

url = "https://finance.naver.com/marketindex/"
response = requests.get(url).text
soup = BeautifulSoup(response, "html.parser")
result = soup.select_one("#exchangeList > li.on > a.head.usd > div > span.value").text

print(f"현재 원/ 달러 환율은 {result}입니다.")
#wfootballTeamRecordBody > table > tbody > tr:nth-child(2) > td.align_l > div > span
#wfootballTeamRecordBody > table > tbody > tr:nth-child(2) > td.selected > div > span
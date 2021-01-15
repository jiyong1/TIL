import requests
import datetime
from bs4 import BeautifulSoup

url = 'https://finance.naver.com/sise/'
response = requests.get(url).text
# print(response.status_code)
soup = BeautifulSoup(response, 'html.parser')
result = soup.select_one("#KOSPI_now").text
now = datetime.datetime.now()

print(result)
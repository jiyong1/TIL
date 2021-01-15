import requests
from bs4 import BeautifulSoup
import datetime

name = input()
url = f"https://api.nationalize.io/?name={name}"
response = requests.get(url).json()
# print(response)
flag = False
for i in response['country']:
    flag = True
    print(f"{name}의 국적은 {float(i['probability'])*100:0.2f}확률로 {i['country_id']}입니다.")

if flag == False:
    print(f"{name}의 국적을 예상할 수 없습니다.")
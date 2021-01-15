import requests
from bs4 import BeautifulSoup

key = 'SJq6idSlitXpK%2BZDyH%2BgJYwz9HOo8HR2htxRSTBTCIxzPDsTVqXsOcz5I5ZrCUHXw4o4CAE6HFdgkZCzsMQSeA%3D%3D'
url = f'http://openapi.airkorea.or.kr/openapi/services/rest/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={key}&numOfRows=10&pageNo=3&sidoName=서울&ver=1.6'

response = requests.get(url).text
data = BeautifulSoup(response, 'xml')
# print(data)

item = data('item')[5]
time = item.dataTime.text
station = item.stationName.text
dust = int(item.pm10Value.text)
dust_cri =''
# print(f'{time} 기준 {station}의 미세먼지 농도는 {dust} 입니다.')
if dust > 150 :
    dust_cri = "매우 나쁨"
elif dust > 80:
    dust_cri = "나쁨"
elif dust >30:
    dust_cri = "보통"
else :
    dust_cri = "좋음"

print(f"{time} 기분 {station}의 미세먼지 농도는 {dust_cri} 입니다.")
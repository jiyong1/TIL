import requests
import pprint

city = "광주"
a = str(city.encode('UTF-8'))
b= a.strip("b'")
c= b.split('\\x')
c= c[1:]
real_city= ('%'+'%'.join(c)).upper()
url = f"http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=i69R9oJG%2FFlwOAEuUTbxjQzaIv8HQ5S1zT10b%2F1yKrvnaBOE%2B8HuPqacb%2BaGZYF3d3apoDqedPmpAtuz5CK0LA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName={real_city}&ver=1.0"
url2 = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=i69R9oJG%2FFlwOAEuUTbxjQzaIv8HQ5S1zT10b%2F1yKrvnaBOE%2B8HuPqacb%2BaGZYF3d3apoDqedPmpAtuz5CK0LA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.0"
response = requests.get(url).json()

total_count = response["response"]['body']['totalCount']
city_dic = response["response"]['body']['items'][4]
txt = f"{city_dic['stationName']}의 미세먼지 농도는 {city_dic['pm10Value']}입니다."

token = ""
api_url = f"https://api.telegram.org/bot{token}"
chat_id = ''
send_url = f'{api_url}/sendMessage?chat_id={chat_id}&text={txt}'
requests.get(send_url)
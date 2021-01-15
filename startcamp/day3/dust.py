import requests
import pprint

city = "광주"
a = str(city.encode('UTF-8'))
b= a.strip("b'")
c= b.split('\\x')
c= c[1:]
real_city= ('%'+'%'.join(c)).upper()
url = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=i69R9oJG%2FFlwOAEuUTbxjQzaIv8HQ5S1zT10b%2F1yKrvnaBOE%2B8HuPqacb%2BaGZYF3d3apoDqedPmpAtuz5CK0LA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName={real_city}&ver=1.0"
url2 = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey=i69R9oJG%2FFlwOAEuUTbxjQzaIv8HQ5S1zT10b%2F1yKrvnaBOE%2B8HuPqacb%2BaGZYF3d3apoDqedPmpAtuz5CK0LA%3D%3D&returnType=json&numOfRows=100&pageNo=1&sidoName=%EA%B4%91%EC%A3%BC&ver=1.0"
response = requests.get(url).json()

# total_count = response["response"]['body']['totalCount']
# chipyeong = response["response"]['body']['items'][4]
# print(f"{total_count}개의 결과를 획득하였습니다")
# print(f"{chipyeong['stationName']}의 미세먼지 농도는 {chipyeong['pm10Value']}입니다")
print(real_city)
#%EA%B4%91%EC%A3%BC
import requests

name = input()
url = f"https://api.agify.io/?name={name}"

response = requests.get(url).json()

print(f"{name}님의 예상 나이는 {response['age']}살 입니다.")

# 매개변수로 전달될 값을 이용해서 http://106.101.9.129 요청을 전달하고 응답을 출력하는 프로그램
# python cli.py ls 형식으로 실행하면 http://106.101.9.129/container/ls 요청을 전달하고 응답 출력

import requests
import sys


cmd = sys.argv[1]
url = f"http://192.168.35.206/container/{cmd}"
response = requests.get(url)
response = response.text[1:-1].replace("\\\"", "\"")


for line in response.split("\\n"):
    print(line)


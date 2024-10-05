# 모듈이란? 파이썬 코드를 포함하는 파일(.py)
# 패키지? 여러 모듈을 포함하는 디렉토리
import math
# print(math.sin(1))
# print(math.cos(1))

# from math import sin, cos
# from math import *
# print(sin(1))
# print(cos(1))
#
# import math as w
# print(w.sin(1))
# print(w.cos(1))
#
# import sys
# # sys 모듈 : 시스템과 관련된 정보를 가지고 있는 모듈
# print("명절줄 인수 : ", sys.argv)
#
# print("실행 경로 : ", sys.path[0])

# import os
# cwd = os.getcwd()
# print(cwd)
#
# #디렉토리 생성
# os.mkdir("test")
#
# #파일 또는 디렉토리 존재
# is_file = os.path.isfile("password.txt")
# print(is_file)
#
# is_dir = os.path.isdir("test")
# print(is_dir)

# os.system("ls")
# os.system("dir")

# 모듈 만들기
# def add(a,b):
#     return a+b
#
# def sub(a,b):
#     return a - b
#
# if __name__ == "__main()__":
#     print(add(1,4))
#     print(sub(4,2))

# ------------------------------------------------
# import 모듈과 패키지
#
# print(모듈과 패키지.add(100,200))
# print(모듈과 패키지.sub(200,20))
#
# get_pwd = password("http://naver.com")
# print(get_pwd)

# ------------------------------------------------
# 파이썬에서는 기본적으로 제공하는 표준 라이브러리 이외에도 다양한 외부 모듈을 제공 합니다
# 외부 모듈은 pip install로 설치 이 후 import 해서 사용
# Beautiful Soup : HTML 또는 XML 파일에서 데이터를 추출하기 위해서 사용하는 파이브러리
# 웹페이지를 크롤링 할 때 사용
# Requests : 서버에 HTTP 요청을 보내고 응답을 받는데 사용하는 라이브러리
# GET, POST, PUT, DELETE 등의 방식을 지원

# import requests
# from bs4 import BeautifulSoup
# url = "https://www.naver.com/weatehr.jsp"
# html = requests.get(url).text
# soup = BeautifulSoup(html, "html.parser")
# print(soup)

# HTTP GET 요청
# respons = requests.get(url)  <-- 웹에서 URL 검색하는 것과 동일하다

# HTML 파싱
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
#
# for loc in soup.select("location")
#     print("도시 : ", loc.select_one("city").string)
#     print("날씨 : ", loc.select_one("wf").string)
#     print("최고기온 : ", loc.select_one("tmn").string)
#     print("최저기온: ", loc.select_one("tmx").string)
#     print("-" * 20)












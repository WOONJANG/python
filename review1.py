# 복습1 (Python)
# 기본 무조건 배열
# 파이썬 웹 서버구축 - flask
# 이클립스 - Java가 설치되어있을 경우 이클립스 사용 X
# IDE 를 구분해서 사용 (JAVA - PYTHON)

# IDE - python 설치
# 그 외에 패키지 - pip install 패키지명
# 패키지 삭제 - pip uninstall 패키지명
# 설치 되어있는 pip 확인 -> pip list
#---------------------------------------#
# python 변수에 자료형 없음
abc = ["a", "b", "c", 10]
# for in(배열 데이터), while (일반 반복문)
print("{}".format(abc[0]))

import random as rd
aaa = rd.randint(4,10)
# from random import *
# aaa = randint(5,10)
print(aaa)

# 문자열 형태
msg = """ 
[이용약관]
테스트입니다.
"""
print(msg)

# 문자열을 세팅 하는 형태
hp = "010-2386-6958"
print(hp[9]) # 6
print(hp[0:3]) # 010 (문자열 0부터 2까지)
print(hp[:8]) # 010-2386 (문자열 처음부터 7까지)
print(hp[9:]) # 6958 (문자열 9부터 끝까지)
print(len(hp)) # 13 (문자열 개수)
print(hp.replace("-", "")) # 01023866958 (- 가 ""으로 바뀜)
print(hp.find("2")) # 4 (4번에 있음)
print(hp.find("<span>")) # -1 없어서 확인 못 함
# findall 무조건 변수로 받아서 배열로 처리
# re 패키지를 가져와서 사용
import re as r
array = r.findall("3", hp)
print(array)

# 변수값 출력 (3.6v 이상)
abox = 3000
cbox = 5000
total = f"{abox}와 {cbox} 부분 금액 입니다."
print(total)

# 경로 출력 \\ 로 설정
print("C:\windows\python") # 일반 문자로 출력
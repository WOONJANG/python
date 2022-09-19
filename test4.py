# 절대값 구하기
print(abs(-100)) # 출력 : 100 # 음수를 양수로 변경
print(pow(2, 3)) # == 2**3
print(max(10, 8)) # 여러개의 값 중 최대값
print(min(9, 1)) # 여러개의 값 중 최소값
print(max(10, 11232, 1223, pow(9, 10), abs(-123120020032323)))
print("---------------")
# abs는 배열 형태로 수정 후 양수로 변경이 가능함 그 외에 방식은 사용허자 않음
# max 및 min 경우는 배열을 사용하지 않아도 숫자를 나열할 경우 큰값과 작은값을 가져옴
print(max(1,-5,8,-7,11,3,-6))
print("---------------")
# round : 반올림
print(round(3.74)) # 출력 : 4
print(round(3.14)) # 출력 : 3
print("---------------")
# round외의 모듈을 사용하는 경우 (floor, ceil)
# 문법에 math없이 사용하는 방식
from math import *
# floor : 내림
print(floor(3.74)) # 출력 : 3
# ceil : 올림
print(ceil(3.14)) # 출력 : 4
print("---------------")
# 해당 모듈에 따른 이름을 선언하고, 문법을 사용함
# 문법에 math 사용하는 방식
import math
print(math.floor(3.74)) # 출력 : 3
print(math.ceil(3.14)) # 출력 : 4
print("---------------")
#랜덤
from random import *
print(random()*10)  # 소수점 아래 포함하여 난수 생성
print(int(random()*10)) # 0 ~ 10 미만의 난수 생성
print(int(random()*10)+1) #1 ~ 10 난수 생성
print(randrange(1,10)) # 1 ~ 10 미만 난수 생성
print(randrange(1,11)) # 1 ~ 11 미만 난수 생성
print(randint(1, 2)) # 1 ~ 2 이하 난수 생성
print(randint(1, 46))
print("---------------")
# 문자열을 출력하는 방식 '''문자''' or """문자"""
msg = """홍길동님 환영합니다.
적립금은 2500원 사용하실 수 있습니다.
"""
print(msg)

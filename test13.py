############################## 응용 문제 ##############################
# 출력 : 2 * 1 ~ 3 * 9 출력

from random import *

for a in range(2,4):
    for b in range(1,10):
        print(str(a) + "*" + str(b) + "=" + str(a*b))
        print(a,"*",b,"=",a*b)
print("---------------")
data = [1, 2, 3, 4, 5]
print(data)
data = [i+1000 for i in data] # 배열값에 기존 배열값을 적용하여 산술식으로 배열을 새롭게 구성
print(data)
print("---------------")
# 다양한 형태로 배열값을 반복문을 통해 변화시킬 수 있음.
person = ["kim", "park", "lee"]
person = [aa.upper() for aa in person]
print(person)
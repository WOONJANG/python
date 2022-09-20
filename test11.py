# 반복문
from random import *

for a in [1, 2, 3, 4, 5]:
    print(a)
for b in range(10):  # 0~9
    print(b)
for c in range(1, 11):  # 1~10
    print(c)
print("---------------")
box = ["red", "blue", "green"]
for d in box:
    print("color : {}".format(d))
print("---------------")
w = 1
while w <= 5:
    print(w)
    w += 1
print("---------------")
ww = 5  # 초기값
while ww > 0:  # 범위값
    print(ww)
    ww -= 1  # +=(++), -=(--)와 같음
print("---------------")
www = 0
while True:  # 루프 사용시 적용 # 초기값있어야함.
    print("")
    print(www)

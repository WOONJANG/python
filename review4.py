# 파이썬 함수
def hungry():
    print("배고파")

z = 0
while True:
    hungry()
    if z==10:
        break
    z += 1

def aaa(a,b):
    print("상품명:{}, 가격:{}" .format(a,b))
    print("상품명:{1}, 가격:{0}" .format(a,b))
aaa("가방",3000000)

import defs as df
result = df.ccc()
print(result)
df.ddd(10, 20)

# -------------class------------ #
class cdatas:
    money = 5000 # 전역변수
    def aaa(self):
        money = 1000 # 지역변수
        # money를 그냥 return하게 되면 error, aaa메소드에서 money 변수를 찾음
        return self.money # 전역변수값을 가져옴
        return money # 지역변수값을 가져옴

cl = cdatas()
result = cl.aaa() # 클래스 안에 여러개의 전역변수가 있으면, 해당 변수값을 바로 가져올 수 있음
print(cl.money)

# 외부 class 로드 

out = df.product()
out.add1(50000)
out.add3()
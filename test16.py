# 편의성 및 함수 이동 방법

# 0001 0002 0003

for number in range(1,30):
    # zfill : 자동으로 숫자 자리수를 맞추는 함수
    print("대기번호 : " + str(number).zfill(3))

# 3자리 마다 , 출력
money = 100000000000
print("{0:,}".format(money))

# 함수 이동
def abc():
    bbb()

def bbb():
    print("함수 이동으로 값을 출력시킴")

abc()
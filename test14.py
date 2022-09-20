# 함수
def aaa():  # def라는 이름을 가지고 있으며 JS의 funtion과 비슷함
    print("함수 호출 완료")

aaa()  # 함수 즉시 실행

def bbb(a):
    print("함수 호출 값은 {0}".format(a))

bbb("홍길동")

def ccc(b, c):
    d = b + c
    return d

z = ccc(5, 10)
print("결과값은 {0} 입니다".format(z))

money = 100000
def bank(umoney):
    if umoney > money:
        msg = "출금하실 금액이 잔액보다 큽니다"
    else:
        m = money - umoney
        msg = str(umoney) + "원 출금 되었습니다. 잔액은" + str(m) + "원 입니다."
    return msg

result = bank(5000)
print(result)

# 함수 인수값에 값을 전달하여 출력하는 형태

def myinfo(username,age,email):
    print("고객명 : ",username,"나이 : ",age,"이메일 : ",email)
    print("고객명 : {0} 나이 : {1} 이메일 : {2}" .format(username,age,email))

myinfo("홍길동",33,"test@test.com") 

#산술연산 기호 및 결과값 출력
print(10%4) # %나머지 구하는 연산기호
print(10/3) # / 소수점도 출력되는 나누기 
print(10//3) # // 소수점 아래 숫자 제외하고 정수로 출력
print(2*3)  # * 곱하기
print(2**3) # ** 2^3 == 2*2*2
print("---------------")
# 부등호
print(10+30 == 50) # 출력 : false
print(10+30 <= 40) # 출력 : true
print(10+30 == 40) # 출력 : true
print(10 != 20) # 출력 : true
print(not(10 != 20)) # 출력 : flase
print("---------------")
# & |
print((10 > 5) and (10 < 5)) # 출력 : false # &&
print((10 > 5) and (3 < 5)) # 출력 : true # &&
print((10 > 5) & (3 < 5)) # 출력 : true # and == &
print((10 > 5) or (10 < 5)) # 출력 : true # ||
print((10 < 5) | (10 > 5)) # 출력 : true # or == |
print((10 < 5) | (4 < 3)) # 출력 : flase # or == |
print("---------------")
# 부등호 여러개를 한번에 비교하여 전체가 모두 맞을 경우 true 그 외 false
print(10 > 20 > 30) # 출력 : false
print(3 > 2 > 1) # 출력 : true
print("---------------")
# 괄호 부분에 포함한 산술연산 부터 실행
print(10+20*10)
print((10+20)*10) 
num = (10+20)*10
print(num)
print("---------------")
# 증감 감소 곱하기 나누기 (+= -+ *= /= %=)
jum = 5
jum += 4
print(jum)
print("---------------")
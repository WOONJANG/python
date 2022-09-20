from random import *    # 라이브러리 (randomm, randrange, randint(한개) < range(다수))
# range는 배열 범위 데이터를 생성하는 클래스
user = range(1, 21)
user = list(user)   # range 사용시, set 또는 list로 변환시키고 출력해야 배열 형태로 출력됨
print(user)
# shuffle : 배열값을 랜덤하게 순서를 변화시킴 (set은 안됨)
shuffle(user)
print(user)
print("---------------")
numbers = range(1, 47)
numbers = list(numbers)
shuffle(numbers)
# sample(배열명, 개수) 배열에서 랜덤하게 개수만큼 뽑아줌 # random => sample은 1개 이상 값을 가져올때
lotto = sample(numbers, 6)
print(lotto)
print("첫번째 당첨번호 : {0}" .format(lotto[0]))
print("두번째 당첨번호 : " + str(lotto[1]))
print("세번째 당첨번호 : %s" % lotto[2])
lo4 = lotto[3]
print(f"네번째 당첨번호 : {lo4}")
print("다섯번째 당첨번호 : {lo5}" .format(lo5=lotto[4]))
print("여섯번째 당첨번호 : {}" .format(lotto[5]))

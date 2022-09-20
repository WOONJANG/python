from random import *
#반복문 + 조건문
# for문과 if를 사용시, 들여쓰기를 주의
array = [9, 12, 17, 22]
for a in range(0, 30):
    if a in array:
        array[a]  # 할 경우 인덱스 값이 없는 부분도 있기때문에 문법오류 발생함
        print(a)
    continue  # 조건에 맞을경우 w++가 적용되어 다음 반복문이 실행
    # break # 해당 조건이 맞을 경우 반복문에서 빠져나옴
print("---------------")
for b in range(0, 30):
    if b in array: # 배열값과 반복되는 값이 같을 경우
        if b > 20: # 그 외 20이상이 될 경우
            break # 반복문 정지
        else: # 그 외
            print(b) # 출력 : 9 12 17 # 조건에 맞는 부분을 출력
print("---------------")
w = 0
while True: # 무한 루프 사용
    if w in array:
        if w < 30:
            print(w)
            w+=1 # 무한 루프에서는 w를 별도로 사용하지 않으므로 +1씩 강제 증가시킴
    else:
        w+=1
        if w > 30: # 무한 루프 but 30이상일 경우 강제 종료
            print(w)
            break
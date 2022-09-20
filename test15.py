# 전역변수, 지역변수

box = "변수값"
box3 = "빈 값" # 최초 전역변수값은 비어있음
# 전역변수는 절대값이 변화가 없음 단, global 
def afunction():
    box2 = "변수값 2"
    global box3 # 전역변수명을 호출
    print(box)
    print(box2)
    print(box3) # 전역변수값을 출력
    box3 = "변수값 3" # afunction 실행시 box3에 문자값이 입력됨
    # 만약 global이 없을 경우는 새로운 지역변수가 생성되며, global적용시 전역변수에 새로운 값을 적용

def bfunction():
    print(box)
    # print(box2) # bfunction 에는 box2 변수가 없음
    print(box3) # 변수값3 이라고 출력됨
    #단, afunction보다 bfunction이 먼저 실행 될 경우 빈값이 출력

afunction()
bfunction()
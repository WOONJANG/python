username = "홍길동"
msg = "적립금"
point = 5
money1 = 1000
money2 = 1500
money = money1 + money2
#str(변수명) : 숫자를 바로 print하지 못하므로 str(변수명) 문자화 시켜서 출력해야 함.
print(username + "님 환영합니다.")
print(username + "님 "+ msg + " 3000원을 사용하셨습니다.")
print(username + "님 "+ msg + " " + str(money) +"원 있습니다.")
msg = "포인트" #같은 변수명이면 값이 바뀜
print(username + "님 현재 골드회원이며, "+ msg +"은(는) "+ str(point) +"% 적립됩니다.")
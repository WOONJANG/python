# %d(숫자) %s(문자, 숫자)
print("포인트 %d이(가) 있습니다." %6000) # 출력 : 포인트 6000이(가) 있습니다.
print("%s님 환영합니다." %"홍길동") # 출력 : 홍길동님 환영합니다.
print("%s님 포인트 %s이(가) 있습니다." %("이순신","5000")) # 출력 : 이순신님 포인트 5000이(가) 있습니다.
print("---------------")
# {}형태의 배열형태의 구성
print("{}님 회원등급은 {} 입니다.".format("유관순","실버회원")) # 출력 : 유관순님 회원등급은 실버회원 입니다.
print("{}님 입금하신 총 금액은 {} 입니다." .format("강감찬",55000 + 200000000)) # 출력 : 강감찬님 입금하신 총 금액은 200055000 입니다.
# 값의 순서를 바꿔서 출력 가능
print("고객님 아이디는 {1} 이며, 가입하신 이름은 {0} 입니다." .format("세종대왕","kings")) # 출력 : 고객님 아이디는 kings 이며, 가입하신 이름은 세종대왕 입니다.
# 변수명 형태로 출력이 가능하며 변수의 값을 외부에서 받아서 출력 가능
print("계산하신 상품은 {product} 이며, 총 결제할 금액은 {money}원 입니다." .format(product="핸드폰", money=650000)) # 출력 : 계산하신 상품은 핸드폰 이며, 총 결제할 금액은 650000원 입니다.
print("---------------")
# py ver 3.6 이상
# 출력 앞에 f를 작성(format의 약어)
color = "red"
car = "제네시스"
print(f"고객님의 자동차 모델은 {car} 이며,\n색상은 {color} 입니다.")
# 출력 : 고객님의 자동차 모델은 제네시스 이며,(줄바꿈 == \n)
#색상은 red 입니다.
print("---------------")
# \ 하나만 입력할 경우는 \n 처럼 특수 언어를 사용하는 형태로 인식함. window server에서 local로 파일을 로드할 경우 \\ 2개 사용 해야함
print("c:\\user\\window\\programmer")

############################## 응용 문제 ##############################
from random import *
word1 = "abcdefghijklmnopqrstuvwxyz"
lens = len(word1)
pw1 = int(random() * lens)
pw2 = int(random() * lens)
pw3 = int(random() * lens)
pw4 = int(random() * lens)
pw = word1[pw1] + word1[pw2] + word1[pw3] + word1[pw4]
print(pw)
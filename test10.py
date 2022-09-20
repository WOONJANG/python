# if문 : == {}
a = 15
if a == 5:
    print("숫자 5 입니다.")
elif a == 10:  # elif == else if
    print("숫자 10 입니다.")
else:
    print("숫자 15 입니다.")
print("---------------")
# input == Scanner(java)와 같은 기능
b = input("좋아하는 숫자를 입력하세요.")
c = int(b) % 2  # input에 입력된 값은 모두 str로 인식하게 되므로 산술시 int로 변환해야 적용됨
if b == 0:
    print("짝수")
else:
    print("홀수")
print("---------------")
person = input("고객 아이디를 입력하세요.")
if person == "hong" or person == "kim":
    print("일반 회원 입니다.")
elif person == "park":
    print("실버 회원 입니다.")
else:
    print("가입되지않은 회원입니다.")
print("---------------")
# 사용자가 입력한 값을 숫자로 자료형 변환을 할 경우
number = int(input("총 입금하실 금액은?"))
if number < 10000:
    print("입금은 최소 10,000원 이상이여야 합니다")
# elif number >= 10000 and number <= 5000000:
elif 10000 <= number <= 5000000: # 입력 범위를 설정하여 조건문 작성
    print("정상적으로 입금이 완료 되었습니다.")
else:
    print("1회 입금 한도는 5,000,000원 까지 입니다.")
    
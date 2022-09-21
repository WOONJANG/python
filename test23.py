# 사용자 입력값에 따른 결과 출력 (예외처리)
try:
    print("두개의 값을 입력하세요.")
    data = []
    number1 = int(input("첫번째 숫자를 입력하세요."))
    number2 = int(input("두번째 숫자를 입력하세요."))
    if number1 >= 1 and number2 >= number1:
        data.append(number1)
        data.append(number2)
    else:
        # raise : 해당 이름을 가진 except를 선정하여 실행되도록 함
        raise OverflowError() 
    print(data)
except OverflowError:
    print("두번째 입력값이 첫번째 입력값보다 커야 합니다.")
# value, zerodivision 등등등
except ValueError: # error가 됐을때 적용되는 부분
    print("숫자만 입력")

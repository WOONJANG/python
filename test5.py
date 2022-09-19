# 문자열 자르기 및 해당 문자열 가져오기(배열 구조이므로 0부터 시작)
gender = "981124-2137213"
print("성별 : " + gender[7]) # 출력 : 2
print("월일 : " + gender[2:6]) # 2이상 6미만 # 출력 : 1124
print("생년월일 : " + gender[:6]) # 무조건 0부터 시작하여 문자열을 가져옴 # 출력 : 981124
print("주민번호 뒷자리 : " + gender[7:]) # 해당 문자열(배열번호 부터) 끝까지 가져옴 # 출력 : 2137213 
print("생년월일 : " + gender[:-8]) # -1부터는 문자열에서 거꾸로 넘버링을 하게됨 # 출력 : 981124
print("---------------")
word = "Python Programming"
# lower : 문자를 모두 소문자로 변경
# upper : 문자를 모두 대문자로 변경
print(word.lower()) # 출력 : python programming
print(word.upper()) # 출력 : PYTHON PROGRAMMING
# is는 문자열에 대한 검토를 할 때 사용하는 문법 isupper, islower
print(word[2].isupper()) # 출력 : false
print(word[2].islower()) # 출력 : true
print("---------------")
print(len(word)) # 출력 : 18 # len == length : 개수
print(len(word[2:10])) # 출력 8 (thon Pro)
print("---------------")
print(word.replace("Python", "Java")) # 출력 : Java Programming
print("---------------")
print(word.index("g")) # 출력 : 10 (10번째에 g가 있다) # 문자열에 대한 노드(위치) 번호를 출력
print("---------------")
i = word.index("P") # 문자열에서 동일한 단어가 있어도 첫번째 찾는 단어에 대한 번호
i = word.index("P", i + 1) # 문자열에 동일한 단어 다음것을 찾아서 출력하는 번호
print(i) # 출력 : 7
print("---------------")
# find : 문자열을 찾을 때 사용 (indexOf와 동일한 기능)
# -1 : 문자열 또는 단어가 없을때
print(word.find("gral")) # 출력 : -1 
print(word.find(" Prog"))
print("---------------")
# count : 해당 문자가 몇개 들어있는지
print(word.count("P")) # 출력 : 2
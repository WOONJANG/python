# 배열로 만들기
age = [10,20,30,40,50,60,70,80,90,100]
print(age[2]) # 출력 : 30
print("---------------")
person = ["홍길동", "이순신", "강감찬"]
print(person[2]) # 출력 : 이순신
print(person)
print(person.index("강감찬")) # 출력 : 2 # person배열에 value값을 찾아서 노드에 있는지 확인
print(len(person)) # 출력 : 3
person.append("유관순")
print(person) # 출력 : ['홍길동', '이순신', '강감찬', '유관순']
# insert는 배열 원하는 위치에 값을 추가
# insert(노드번호, 추가할 값)
person.insert(1, "세종대왕")
print(person) # 출력 : ['홍길동', '세종대왕', '이순신', '강감찬', '유관순']
#pop() : 값을 뒤에서 부터 가져옴
print(person.pop()) # 출력 : 유관순
print(person.pop()) # 출력 : 강감찬
print(person.pop()) # 출력 : 이순신
print("---------------")
numbers = [5,8,7,1,9,3,2,6]
# sort() : 오름차순
numbers.sort()
print(numbers) # 출력 : [1, 2, 3, 5, 6, 7, 8, 9]
# reverse() : 내림차순
numbers.reverse()
print(numbers) # 출력 : [9, 8, 7, 6, 5, 3, 2, 1]
# clear() : 값을 다 지움
numbers.clear()
print(numbers) # 출력 : []
print("---------------")
datas1 = ["hong", "홍길동", 33, 3000, False]
datas2 = ["면도기", "신발", "바지", "이어폰"]
# datas2에 있는 배열값을 datas1에 종속시킴
# 배열값을 종속 시킬때는 변수로 받아서 처리하지 않음
datas1.extend(datas2)
datas3 = datas1 + datas2
print(datas1) # 출력 : ['hong', '홍길동', 33, 3000, False, '면도기', '신발', '바지', '이어폰']
print(datas3) # 출력 : ['hong', '홍길동', 33, 3000, False, '면도기', '신발', '바지', '이어폰', '면도기', '신발', '바지', '이어폰'] (위에서 추가된 상태에서 + datas2해서 두번뜸)
print("---------------")
# 키 값이 있는 배열 형태
infodata = {"mid":"hong", "mname":"홍길동","age":33, "point":3000}
print(infodata["age"]) # 출력 : 33 # 배열에 있는 키값으로 로드
print(infodata.get("mid")) # 출력 : hong # get이라는 함수를 이용해서 키 배열값을 가져오는 형태
# in은 키배열에 해당 키값이 있는지를 확인하는 문법
print("age" in infodata) # 출력 : true
print("tel" in infodata) # 출력 : false
# 키배열에는 append, insert를 사용하지 않고 수정 가능
# 배열에 키값 추가
infodata["tel"] = "01023456789"
print(infodata) # 출력 : {'mid': 'hong', 'mname': '홍길동', 'age': 33, 'point': 3000, 'tel': '01023456789'}
# 배열 키값으로 수정
infodata["age"] = 50
print(infodata) # 출력 : {'mid': 'hong', 'mname': '홍길동', 'age': 50, 'point': 3000, 'tel': '01023456789'}
# 키배열값 삭제
del infodata["mid"]
print(infodata) # 출력 : {'mname': '홍길동', 'age': 50, 'point': 3000, 'tel': '01023456789'}
infodata["mid"] = ""
print(infodata) # 출력 : {'mname': '홍길동', 'age': 50, 'point': 3000, 'tel': '01023456789', 'mid': ''}
print(infodata.keys()) # 키 명만 출력 == Object.keys(javascript) # 출력 : ['mname', 'age', 'point', 'tel', 'mid']
print(infodata.values()) # 값만 출력 # 출력 : ['홍길동', 50, 3000, '01023456789', '']
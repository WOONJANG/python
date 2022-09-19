# 튜플 : 셀 수 있는 수량이 나열된 형태, 배열([],{}) X
subject = ("자바", "파이썬", "서블릿")
print(subject[1]) # 출력 : 파이썬

a1 = "홍길동"
a2 = "hong@test.com"
a3 = "M"
a4 = (a1,a2,a3)
print(a4) # 출력 : ('홍길동', 'hong@test.com', 'M')
print("---------------")
# 세트(집합) : 중복된 데이터는 출력이 되지 않도록 함
listdata = {100,200,100,200,500,600,700} # 출력 : {100, 500, 200, 600, 700}
print(listdata)
print("---------------")
listdata2 = {"홍길동","이순신","홍길동","강감찬"} # 출력 : {'홍길동', '이순신', '강감찬'}
print(listdata2)
print("---------------")
# []로 시작하는 배열 형태는 중복 데이터가 있어도 모든 값을 출력 함
listdata3 = [100,200,300,200,600,200,500]
print(listdata3) # 출력 : [100, 200, 300, 200, 600, 200, 500]
listdata3.append(1800)
listdata6 = set([100,200,300,200,600,200,500]) # set을 적용시 [] => {} 인식 시킴
listdata6.add(800)
listdata6.remove(200)
print(listdata6) # 출력 : {800, 100, 300, 500, 600}
print("---------------")
listdata3_1 = {100,200,300,200,600,200,500}
print(listdata3_1) # 출력 : {100, 500, 200, 600, 300}
print("---------------")
listdata4 = set([700,300,200]) # set : 교집합 사용시 주의 할 점 : 비교 배열 {}이며, set은 []로 표현
print("---------------")
print(listdata3_1 & listdata4) # 출력 : {200, 300} # 3_1과 4 배열 중 4 배열을 기준으로 3_1의 값을 가져옴
print(listdata3_1.intersection(listdata4)) #intersection은 &로 대체되었음
print("---------------")
print(listdata3_1 | listdata4) # 출력 : {700, 100, 500, 200, 600, 300} # 합집합
print(listdata3_1.union(listdata4)) # union = |
print("---------------")
print(listdata3_1 - listdata4) # 출력 : {600, 100, 500} # 차집합
print(listdata3_1.difference(listdata4)) # difference = -
print("---------------")
# type == typeof 동일한 기능
box1 = {"블랙커피", "아메리카노"} # set
box2 = ["블랙커피", "아메리카노"] # list
box3 = {"product":"블랙커피","money":5100}
print(type(box1))
print(type(box2))
box1 = list(box1) # set => list 변환
print(type(box1))
box2 = set(box2) # list => set 변환
print(type(box2))
box3 = list(box3) # 출력 : ['product', 'money']
box3_1 = list(box3.values()) # 출력 : ['블랙커피', 5100]
 
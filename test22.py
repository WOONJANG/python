# 다중 상속
class box: # 첫번째 상속
    def __init__(self, data1):
        self.data1 = data1


class box2: # 두번째 상속
    def __init__(self, data2):
        self.data2 = data2


class box3(box, box2): # 다중 상속 이용(box,box2 로드)
    def __init__(self, data1, data2, data3): 
        self.data3 = data3 # box3에 대한 값을 self로 이관
        box.__init__(self, data1) # 상속값을 return
        box2.__init__(self, data2) # 상속값을 return
        print("데이터 값 : {0}, {1}, {2}" .format(self.data1, self.data2, self.data3))

a = box3("홍길동", "이순신", "강감찬") # 인자값을 box3로 보냄
print(a)
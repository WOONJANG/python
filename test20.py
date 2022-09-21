# class 선언 방식 및 메소드 형태
class box:
    # __init__ 클래스 호출시 바로 실행되는 함수, class하나에 한번만 선언
    def __init__(self, a, b, c):
        # self == this(java)
        self.a = a
        self.b = b
        self.c = c
        print("값은 {0},{1},{2}" .format(self.a, self.b, self.c))

    def abc(self):  # 일반 메소드
        print(self.c)


box(1, 4, 6)  # __init__에 인자값을 전달
box("홍길동", 146, 25)
cl = box("hong", "25", "100")  # __init__에 인자값을 전달하면서 setter 형태
cl.abc()  # 출력 : 100 # abc메소드를 로드하여 getter 형태
print("---------------")


class box2:
    def __init__(self, name, id, pw):
        self.name = name
        self.id = id
        self.pw = pw

    def abc(self, email): # 일반 메소드에 추가 인자값을 적용
        print("고객명 : {0}, 아이디 : {1}, 이메일 : {3}" .format(self.name, self.id, self.pw, email))


data = box2("이순신", "GGOBUK", "a12345") # __init__에 값을 등록
data.abc("YI@test.com") # abc메소드에 추가로 값을 등록


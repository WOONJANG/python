import pickle as io # 파일 저장, 읽기

# w : 텍스트 저장(write), wb : 저장(dump) + 바이너리
# r : 텍스트 읽기(read), rb : 읽기(load) + 바이너리

# pf = open("array.jangwoon","wb")
# data = [1,2,3,4,5]
# io.dump(data, pf)

rf = open("array.jangwoon","rb")
reslut = io.load(rf)
print(reslut)
rf.close()
# 문자 전용 저장 박식
'''
pf = open("array.txt","w")
data = "홍길동님 ㅋㅋㅋ"
data2 = 25000
pf.write(str(data2))
pf.close()
'''
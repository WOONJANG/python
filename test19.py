# pickle : json같은 데이터 객체 파일
import pickle
data = {"고객명":"홍길동","나이":25,"취미":["볼링","축구","야구"]}
# wb == w(파일 생성(쓰기) 및 저장)(인코딩이 별도로 필요하지 않음)
files = open("file.pickle","wb")
pickle.dump(data, files) # dump 객체를 생성 및 저장
files.close()
print("---------------")
files2 = open("file.pickle","rb")
loadfile = pickle.load(files2)
print(loadfile)
print("---------------")
# with을 사용해서 이용되는 pickle
with open("file.pickle","wb") as files3: # as files3라는 별명 선언
    pickle.dump(data, files3)

with open("file.pickle","rb") as files4:
    loadfile2 = pickle.load(files4)

print(loadfile2)
#with로 파일을 저장하는 형태
with open("abc.txt","w") as textfile:
    textfile.write(data)
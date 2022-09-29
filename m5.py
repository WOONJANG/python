import matplotlib.pyplot as mpt
import mfont

days=[7,8,9]
azn=[100,156,112] #아스트라제네카
pfz=[95,112,198] #화이자
sen=[92,88,76] #얀센
mod=[74,69,87] #모더나

#plot 선으로 이루어진 그래프
mpt.plot(days,azn,label='아스트라제네카',marker="o")
mpt.plot(days,pfz,label='화이자',marker="o")
mpt.plot(days,sen,label='얀센',marker="o")
mpt.plot(days,mod,label='모더나',marker="o")
mpt.xticks(days,['7월','8월','9월'])

for idx,txt in enumerate(azn):
    mpt.text(days[idx],azn[idx]+1,txt,ha="center")
    
for idx,txt in enumerate(pfz):
    mpt.text(days[idx],azn[idx]+10,txt,ha="center")
    
for idx,txt in enumerate(sen):
    mpt.text(days[idx],azn[idx]+15,txt,ha="center")
    
for idx,txt in enumerate(mod):
    mpt.text(days[idx],azn[idx]+20,txt,ha="center")        

mpt.legend(ncol=4) #ncol: 1줄에 n개의 라벨을 출력하는지 선정. 기본값 1
mpt.show()
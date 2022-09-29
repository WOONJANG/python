import pandas as pd
import matplotlib.pyplot as mpt
import mfont

# 총 인구수
data = pd.read_excel("person.xlsx", usecols="D:G")

# 남성 인구수
man = pd.read_excel("person.xlsx", usecols="AA:AD")

# 여성 인구수
woman = pd.read_excel("person.xlsx", usecols="AX:BA")

# data.T or data : 인덱스에 대한 위치가 변경됨
# 여러 데이터중 1개만 사용하는 사항(여러데이터를 출력할 경우 bar그래프가 올바르게 반영되지 않음)
# mpt.figure(figsize(10,8))
# titles = data.columns;
# mandata = man.loc[0] # 데이터 1개씩 가져옴
# print(mandata)

# bar 그래프 (남성 데이터) # //100 (숫자 단위가 '만'단위가 넘어갈 경우)
# subplots, subplot : 한개의 그래프에 여러 데이터를 보여줄 때 사용 
# mpt.subplot(0,0,1)
# mpt.subplot(0,1,2)
fig, ax1 = mpt.subplots(figsize=(10, 8))
titles = data.columns
mandata = man.loc[0]//50
ax1.bar(data.columns, mandata, color="orange", label="남성")
ax1.set_ylim(0, 30000) # 세로 데이터의 최대값
ax1.set_ylabel("남성 0세 ~ 19세") # 왼쪽 데이터 표에 대한 설명
mpt.legend()
# 반복문으로 해당 값을 그래프 위에 출력
for idx, txt in enumerate(mandata):
    ax1.text(idx, txt+500, format(txt,","), ha='center',color="blue")

# plot 그래프 (여성 데이터) # bar 그래프가 남성 데이터와 겹치지 않도록 하기 위해
womandata = woman.loc[0]//50 # // 50 (숫자 단위가 '만'단위가 넘어갈 경우)
# twinx, twiny :
ax2 = ax1.twinx()  # 2개 좌표를 겹침 # 그래프 데이터에 별도의 수치값을 표현 (ax1에 대한 수치 포함)
ax2.set_ylim(0, 30000)
ax2.set_ylabel("여성 0세 ~ 19세") # 추가 수치값에 대한 도움말을 출력
ax2 = mpt.plot(data.columns, womandata, color="red", marker="o", label="여성")
mpt.legend(loc='center left')
# 선 그래프에 해당 수치값을 표현
# 그래프에 수치값 표현시 주의점 : 값을 나누어서 표현할 경우 +1, +10 표현이 잘 안됨(더 큰 숫자를 입력해야 함)
for idx2, txt2 in enumerate(womandata):
    mpt.text(idx2, txt2+500, format(txt2,","), ha='center',color="red")

mpt.show()

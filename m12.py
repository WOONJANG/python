#산점도 응용부분
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#scatter:x축, y축이 무조건 필요
data=pd.read_csv("movie.csv",encoding="euc-kr")
#c: color + cmap (자동색상)

#scatter에서 text사용시 x축 y축에 대한 값이 모두 int로 이루어져 있어야 반복문으로 적용할수 있습니다.
for a, txt in enumerate(data["영화관"]):
    mpt.scatter(data["지역"],data["관객수"],sizes=data["관객수"]*5,c=data["관객수"],label=data["관객수"])
    mpt.text(data["지역"],data["관객수"], txt)

mpt.colorbar()
mpt.xlabel("지역")
mpt.ylabel("관객수")
mpt.show()
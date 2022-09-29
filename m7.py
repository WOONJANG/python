#csv파일 그래프화 적용(plot)
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#pandas 입력 => matplotlib 출력

data = pd.read_csv("area.csv", encoding="euc-kr")
mpt.plot(data['지역'],data['휘발유'], label='휘발유')
mpt.plot(data['지역'],data['경유'], label='경유')
mpt.plot(data['지역'],data['LPG'], label='LPG')
mpt.legend()
#그래프를 가시화 형태로 변경 (axis:라인을 표시. x=세로줄 y=가로줄)
mpt.grid(axis='x', linestyle='--')
mpt.show()
#다중 그래프 출력 형태
import pandas as pd
import matplotlib.pyplot as mpt
import mfont

#axs :다중 표를 제작할 때 사용하는 함수
#subplots : 가로,세로 개수만큼 생성
#figsize : 그래프의 사이즈 설정
''' 
a,axs=mpt.subplots(2,2,figsize=(15,10))
a.suptitle("각 파트별 데이터 분석")
'''
''' 
a,axes=mpt.subplots(2,2,figsize=(15,10))
a.suptitle("각 파트별 데이터 분석")
'''
a,axs=mpt.subplots(2,2)
a.set_size_inches(15,10)
#subplots_adjust:가로,세로에 대한 여백(html의 margin같은 개념)
mpt.subplots_adjust(wspace=0.5,hspace=0.5)
a.suptitle("각 파트별 데이터 분석")
mpt.show()
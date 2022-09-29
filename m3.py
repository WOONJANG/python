import matplotlib.pyplot as mpt
import mfont

x=[15,20,7,36]
#linewidth : 그래프 선 두께. 1=1px
#marker : 각 포인트별로 모양을 말합니다. 마커 스타일 o(원형), v(삼각형), x(x) 등등
#markerfacecolor:마커 배경색 채우기
#markeredgecolor:마커 테두리 색
#linestyle : solid, dashed, dotted 등
#color :  선색상
# mpt.plot(x, color='red', linestyle='dashed', label='2022년 취업통계', linewidth=2, marker='o', markeredgecolor='orange', markerfacecolor='red')
#축약어로 세팅된 그래프 형태
mpt.plot(x,color="red",mfc="blue",mec="green",ls="dashed")
mpt.legend(loc=(0.1,0.1)) #label에 대한 탭을 표현합니다. 
# loc =(x축,y축) 위치. 0 ~ 1 사이값으로 위치 잡아야함.
#dpi(100 기본) : 200, 300 .해상도 조절. 이미지 저장 시 그래프를 크게 저장할 수 있음.
mpt.savefig('graph1.png', dpi=300) #savefig 이미지로 저장하는 함수
mpt.show() #무조건 제일 밑에서 실행
#import 할때 파일명과 모듈명이 같으면 모듈 로드 안됨.
# from pandas import * ->명칭없이 사용 할 수 있음
import pandas as pd # 명령어 앞에 pd. 붙여야함

#Series => Time, Num, Data (간격에 맞춰서 배치된 데이터들의 값)
data = pd.Series([10,20,30,40]) #Series로 배열값을 로드 (인덱스를 자동으로 설정함)
# print(data)

#index 기본숫자 (0부터 시작), index를 이용하면 데이터 인덱스 별명 명칭을 적용할 수 있음
data2 = pd.Series([17,19,20,17,16,15,16], index=['월','화','수','목','금','토','일'])
# print(data2['토']) #지정된 index 별명을 출력하실 수 있습니다.

array = {
    "username" : ['홍길동','이순신','강감찬'],
    "userage" : ['30','46','27'],
    "usercp" : ['SKT','KT','KT']
    }
#일반 python 형태의 배열출력
# print(array['username'])
pr = pd.DataFrame(array) #DataFrame을 이용해서 키가있는 배열을 시각화
# print(pr) 
#키에는 '', "" 붙여야함
#[['키이름','키이름']] : 원하는 키이름의 데이터만 시각화 합니다.
# print(pr[['username','usercp']])

#키배열에 index명을 변경
pr = pd.DataFrame(array,index=['no1','no2','no3'])
# print(pr)

#컬럼값을 위치 변경 (columns 이용)
pr2 = pd.DataFrame(array, columns=['usercp','username','userage'])
print(pr2)

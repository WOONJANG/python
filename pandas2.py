import pandas as pd
data = {
    'area' : ['서울','경기','제주'],
    'gas' : [1150,1200,980],
    'diesel' :[1860,1845,1998],
    'gasoline' : [1750,1700,1810]
    }

pr = pd.DataFrame(data)
pr.index.name='유가' #index.name : 인덱스 리스트에 목차이름 적용할때 사용 
# print(pr)

pr2=pd.DataFrame(data)
#index번호를 데이터 키값에 맞춰서 변동시킨 형태
print(pr2.set_index("area"))


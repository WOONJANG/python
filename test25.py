# test24.py를 로드

# 첫번째 방법
# import test24
# test24.aaa("우주")
# result = test24.bbb(136)
# print(result)
# test24.ccc("오늘의 IT 주요뉴스","데일리뷰글")
print("---------------")
# 두번째 방법
# 모든 함수는 test24.py에 적용 되도록 코딩
from test24 import *
aaa("우주")
result = bbb(136) # retur 함수는 test25.py에서 출력
print(result)
ccc("오늘의 스파이더맨 주요뉴스","데일리뷰글")
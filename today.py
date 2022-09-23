from datetime import *

# 오늘 날짜 + 시간
today = datetime.now()
print(today)

# 오늘 날짜
day = today.date()
print(day)

# 지금 시간
time = today.time()
# replace(microsecond=0) 초 부분 소수점 삭제
print(time.replace(microsecond=0))

# 시간을 문자열로 변환 -> DB저장시 필요
datetime = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
print(datetime)
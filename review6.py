# 예외처리 try ~ except

try: # 정상처리
    a = "123a"
    b = int(a)
    print(b)
except: # 예외처리
    print("에러발생")
finally: # 프로세서 종료
    print("모든 정상처리가 완료")
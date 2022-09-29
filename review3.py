# # 파이썬 배열 선언시 중요사항
# adata1 = {10, 5, 6, 7, 6, 3, 10, 6}  # 중복삭제 {}
# print(adata1)  # {3, 5, 6, 7, 10}
# adata2 = [10, 5, 6, 7, 6, 3, 10, 6]  # 중복데이터 출력 []
# print(adata2)


# # 배열값을 반복문으로 가져오는 형태
# for no in adata2:
#     print(no)

# # for문 배열 형태2
# adata3 = {"data1": [1, 2, 3, 4], "data2": ["5", "6", "7", "8"]}
# for k in adata3:
#     for kk in adata3[k]:
#         print(kk)  # 1/2/3/4/5/6/7/8

# # for문 배열 형태3
# adata4 = [100, 200, 300, 400, 500]
# # enumerate : 인덱스, 배열값
# for idx, no in enumerate(adata4):
#     print(idx)  # 0/1/2/3/4
#     print(adata4[idx])  # 100/200/300/400/500
#     print(no)  # 100/200/300/400/500

# while문
w = 0
while w <= 5:
    print(w) # 0/1/2/3/4/5
    if w==2:
        break 
        # continue : 반복순서를 넘기는 형태
        # break : 반복문 정지
    w += 1 # ++, -- (없음) # +=, -=(증감)

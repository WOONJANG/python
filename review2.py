# 배열 형태의 데이터 {} []
a = 10
b = 20
c = 30
arrary = [a, b, c]
print(arrary)

adata1 = [1, 2, 3]
adata2 = [100, 200, 300]
adata3 = adata1 + adata2
adata4 = [adata1, adata2]
print(adata3)  # [1, 2, 3, 100, 200, 300]
print(adata4)  # [[1, 2, 3], [100, 200, 300]]
adata1.extend(adata2)  # extend 사용시 신규 변수를 생성할 필요 없이 기존에 있는 변수를 출력
print(adata1)  # [1, 2, 3, 100, 200, 300]

#---------------------------------------#

zdata1 = {1, 2, 3, 4}
print(zdata1)
zdata2 = {"key1": "홍길동", "key2": "이순신"}
print(zdata2["key1"])  # 홍길동

#---------------------------------------#

kdata1 = {"kdata": [1, 2, 3]}
print(kdata1["kdata"])  # [1, 2, 3]
print(kdata1.get("kdata")) # [1, 2, 3]
print(kdata1.keys()) # dict_keys(['kdata'])
print(kdata1.values()) # dict_values([[1, 2, 3]])

#---------------------------------------#

person = ("홍길동", "이순신") # 파이썬에만 있는 배열 구조형태
print(person[1]) # 이순신

(aa, bb, cc) = ("a1","b1","c1")
print(bb) # b1
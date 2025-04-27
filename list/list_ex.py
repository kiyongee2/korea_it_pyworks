# 리스트 자료구조

cart = "라면" #변수
print(cart)

"""
리스트(list) 
- 여러 개의 자료를 저장하는 자료 구조이다.
- 대괄호([])를 사용
- 요소에 접근할때 위치(인덱스)를 사용(맨앞: 0번, 맨뒤: -1)
"""
carts = ["라면", "우유", "토마토", "콩나물"]

# 리스트 객체 출력
print(carts)

# 특정 요소(element) 검색
print(carts[0])
print(carts[1])
print(carts[2])
print(carts[-1])
print(carts[-2])

# 요소 수정
carts[1] = "생수"

print(carts)
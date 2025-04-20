# 조건문
# 나이가 15세 이상이면 "관람가" 출력
age = input("나이를 입력하세요: ")
age = int(age)
"""
if age >= 15: #조건식 True이면 실행됨 
    print("관람가")  #들여쓰기(indent)
print("나이는 " + str(age) + "세 입니다.")
"""

# 나이가 15세 이상이면 "관람가", 아니면 "관람불가" 출력
if age >= 15:
    print("관람가")
else:
    print("관람불가")
print("나이는 " + str(age) + "세 입니다.")

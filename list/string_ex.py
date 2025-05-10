
alpha = ['a', 'b', 'c', 'd']

# 인덱싱
print(alpha[2])

# 슬라이싱(범위로 검색 - ':' 사용)
print(alpha[0:3]) # 종료값 = 종료인덱스-1
print(alpha[0:-1])
print(alpha[0:])  # 마지막 값까지 추출
print(alpha[:])   # 마지막 값까지 추출

# 문자열은 특별한 1차원 리스트이다.
f = "apple"
print(f[0])
print(f[2])
print(f[-1])
print(f[:])

s = "20250510Rainy"
# 연도 추출
year = s[:4]  #끝 -> 끝인덱스-1
print(year)

# 월일 추출
day = s[4:8]
print(day)

# 날씨 추출
weather = s[8:]
print(weather)

print(year + '.' + day + '.' + weather)
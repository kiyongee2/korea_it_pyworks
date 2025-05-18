# 시간 관련 모듈
import time

# 시간은 초로 계산됨(1970. 01. 01 자정 이후부터 지금까지 흐른시간)
print(time.time()) # 1747535857.981002

# 일로 환산
print(round((time.time() / (24*60*60))))  #20226일

# 년으로 환산
print(round(time.time() / (365*24*60*60)))  # 55년 
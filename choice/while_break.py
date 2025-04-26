# 반복 조건문
"""
 'y'키 입력 -> "계속 반복"
 'n'키 입력 -> "반복 중단"
  y/n 이외의 키 -> "키를 잘못눌렀습니다."

"""
while True:
    answer = input("반복을 계속 할까요?(y or n 입력): ")
    if answer == 'y' or answer == 'Y':
        print("계속 반복")
    elif answer == 'n' or answer == 'N':
        print("반복 중단")
        break
    else:
        print("키를 잘못눌렀습니다.")
        
print("프로그램 종료!")













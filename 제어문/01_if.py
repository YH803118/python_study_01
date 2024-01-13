#IF

# 들여쓰기가 매우 중요함.
menu = True
test = [1, 2, 3]

if menu:
    print("참일 경우")
    # print("참일 경우")
    #     print("절대로 들여쓰기 길이를 맞춰")
    # 들여쓰기를 맞추지 않을 경우 에러 발생
else:
    print("거짓일 경우")

# and : 둘 중 하나만 참이어도 참
# or : 모두 참이어야 참
# not
    
# in, not in : 포함 여부
if 1 in test:
    print('들어있음')
else:
    print('안들어있음')

# elif (= else if)
if 4 in test:
    print('들어있음')
elif 1 in test:
    print('들어있음')
else:
    print('안들어있음')

score = 100
msg = "success" if score >= 60 else "failure"
# 조건문을 사용한 정의도 가능함.
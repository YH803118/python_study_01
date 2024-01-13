#FOR

# for num in [1,2,3]:
#     print(num)

a = [(1,2),(3,4)]
for (first, last) in a:
    print(first+last)

# range 함수.
a = range(10) # 0~9까지의 숫자 리스트 객체를 생성
# = range(0,9)
print(a)
add = 0
for b in range(10):
    add += b
print(add)

a = range(5)
result = [num * 3 for num in a]
# 연산식이 먼저 들어가네 if도 그렇고 말이죵
print(result)
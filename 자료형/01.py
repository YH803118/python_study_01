a = "first test!"
fl = 3.2352443
print(a * 3)
print(len(a),a[3], a[0:5], a[:5]) 
# print문 내부는 +로 연결하는게 아닌 쉼표로 연결
print("test 문자열:%s 정수:%d 부동소수:%f" % ("asdf", 3, fl))
# 얘도 문자열 내에 포맷코드로 대입 가능.
print("%10s" % "test")
# 전체길이 10칸. 기본적으로 오른쪽정렬
print("%-10s" % "test")
# 음수로 지정할 경우 왼쪽정렬
print("%.4f" % 3.423522)
# 소수점절단
# testchar = "format test {0} {1}".format("start", "!!!!")
testchar = "format test {fir} {sec}".format(fir="start", sec="!!!!")
print(testchar) # 문자열에 이런식으로 포맷함수를 붙여넣을수도 있다.
test = "{0:>10}".format("hi")
test = "{0:=^10}".format("hi") # 공백을 =로 채워줌.
test = "{0:0.4f}".format(fl) # 소수점자르기
print(test) # 우측정렬. :<10 _좌측정렬. :^10 _가운데정렬
print("{{ and }}".format()) # 포맷붙어있을때 중괄호 갈기는법

a.count('t') # 해당 문자 갯수 세기
a.find('t') # 해당 문자 위치. 없으면 -1
a.index('t') # 해당 문자 위치. 없으면 에러

print(",".join('abcd')) # 문자열 삽입
li = ['a', 'b', 'c', 'd']
print(li, ":".join(li)) # 리스트 출력에도 활용

# a.upper() a.lower() 대문자로, 소문자로
# lstrip rstrip strip 좌,우,좌우 공백 지우기
b = a.replace("test", "nonogram")
# replace의 경우 문자열 교체. 하지만 바뀐채로 다시 저장되지 않음.
# 즉시 출력하거나 다시 변수에 담아야함.
print("resplace test :", b)

a.split()
print("split test :", a)
b = a.split()
print("split test :", b)
# 문자열을 나누는 split도 replace와 동일
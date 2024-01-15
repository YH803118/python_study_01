# LIST

li = [1,2,3,4,5]
# 대괄호를 사용해 리스트 정의
li1 = list() # 빈 리스트
li2 = [] # 빈 리스트
print(li, li1, li2)

print(li[:2])
# 슬라이싱

li3 = [3,6,9]
print(li+li3, li3*3) # 리스트 더하기, 리스트 반복
print(len(li3))

del li3[0] # 리스트 요소 삭제. del 객체
print(li3)

li3.append(1) # 리스트 요소 추가
print(li3)
li3.sort() # 리스트 정렬. 출력값이 없다.
# reverse로 뒤집을 수 있음.
print(li3)

li3.index(1) # 여기도 역시 index 가능. 없으면 에러
li3.insert(1, 23) # 삽입
print(li3)
li3.remove(23) # 인덱스값이 아닌 실제값을 삭제(하나만)
print(li3)

print(li3.pop()) # 맨 끝요소 빼서 출력. 실제로도 맨끝값은 삭제
# li3.count(1) 갯수 세기
#FILE

path = "C:/Users/User/Desktop/python/start/03_입출력"

# f = open("C:/Users/User/Desktop/python/start/03_입출력/new_File.txt", 'w', encoding="UTF-8-sig")
# r - 읽기 모드, w - 쓰기, a - 파일끝에 새로운 내용을 추가할 때
# encoding="UTF-8" - 한글 깨짐 방지
# encoding="UTF-8-sig" - 한글 깨짐 방지2, csv같은 애들에 사용

# i = input("내용 입력 : ")
# f.write(i)
# f.close()

f1 = open(path+"/new_File.txt", 'r', encoding="UTF-8")

# while True:
#     line = f1.readline()
#     if not line: 
#         print("더 읽어올 내용이 없습니다.")
#         break
#     else: 
#         print(line)

# readlines - 줄별로 리스트를 만들어옴
line = f1.readlines()
for i in line:
    if not i: 
        print("더 읽어올 내용이 없습니다.")
        break
    else: 
        print(i.strip())
# strip() 줄바꿈문자 제거

# read - 파일 내용을 문자열로 긁어옴
data = f1.read()
print(data)

f1.close()

# with문을 통해 close문 호출 없이 자동으로 파일을 닫을 수 있다.
with open(path+"/new_File.txt", 'a', encoding="UTF-8") as f2:
    f2.write("\nwith문을 통한 문자열 추가")
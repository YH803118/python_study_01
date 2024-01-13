#WHILE

# 조건문이 true인 동안 반복
# 조건문이 false면 탈출
menu = 0
while menu < 3:
    menu += 1
    print('%d회 반복중' %menu)
    if menu == 3:
        print('반복 종료')

prompt = """
1. Add
2. Del
3. List
4. Quit
Enter number: """

# switch문 같은 느낌이죠?
number = 0
while number != 4:
    print(prompt)
    number = int(input())

# 여기도 역시 if - break문을 통해 강제탈출 할 수 있다.
# 역시 continue로 처음(조건문)으로 돌아갈 수도 있고.
# 그냥 컨트롤C로도 탈출 가능.
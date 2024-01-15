#FUNCTION

def function_name(a, b):
    return a+b

a = 10
b = 15
c = function_name(a, b)


# 변수의 갯수를 모를때. *를 붙여주면 튜플로 만들어준다.
def add_many(*ar):
    a = 0
    for i in ar:
        a += i
    return a

print(add_many(1,2,3))

# **를 붙여주면 딕셔너리의 형태로
def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a=1, b='foo')

# 함수 밖의 변수도 global을 통해 변경 가능
def global_a():
    global a
    a = a + 5

global_a()
print("a = %d" %a)

# lambda : 간단한 함수를 생성. def과 동일한 기능
lamb_fun = lambda a, b: a+b
print(lamb_fun(5, 7))
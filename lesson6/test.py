print('hello')
a = input('Input a: ')
b = input('Input b: ')
try:
    print(int(a) + int(b))
except ValueError:
    print('Неправильний тип змінної')


print('hello')

def our_program():
    num = int(input("Enter integer (0 for output): "))
    sum = 0
    while num != 0:
        for i in range(num + 1): # 11 ->  0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
            sum += i
        num = int(input("Enter integer (0 for output): "))


our_program()


def print_max(a, b):
    if a > b:
        print(f'a = {a} > b = {b}')
    elif a < b:
        print(f'b = {b} > a = {a}')
    else:
        print("a == b")


print_max(10, 15)
print_max(10, 7)

def print_max1(b=5, a=3):
    if a > b:
        print(f'a = {a} > b = {b}')
    elif a < b:
        print(f'b = {b} > a = {a}')
    else:
        print("a == b")


print_max1()
print_max1(10, 12)

print('daw', end='')
print('daw')

print('daw')
print('daw')


def plus(a, b):
    c = a + b
    return c


result = plus(5, 10)
print(result)


x = 50

def func():
    x = 2
    print(id(x))


func()
print(id(x))
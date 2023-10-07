# Цикли
# цикл for
# цикл while
# яблука
# груші
# масло
# сир
# ковбаса


# apple
fruit = 'apple'
for char in fruit:
    print(char)

print('hello world')

devices = ['iphone 11', 'iphone 12', 'iphone 13']
for device in devices:
    if device == 'iphone 11':
        print('Ура я маю 11-й айфон')

a = 1
while a <= 5:
    print(a)
    a = a + 1  # a = 1 + 1
    # a = 2 + 1
    # a = 3 + 1
    # a = 4 + 1
    # a = 5 + 1



a = 0
while True:
    print(a)
    if a >= 20:
        break
    a = a + 1


while True:
    user_input = input('Enter: ')
    print(user_input)
    if user_input == 'exit':
        break

a = 0
while a < 6:
    a += 1
    if a % 2 == 1:
        print('непарне')
        continue
    print(a)


while True:
    age = input('age: ')  # '10'
    number = input('number = ')
    number = int(number)

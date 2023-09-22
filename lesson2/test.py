# умовне виконання -> використання умов для управління потоком виконання
# цикли -> повторення блока інструкцій поки виконується якась умова
# винятки -> виконання блоку інструкцій в випадку помилки
print('hello world')

age = int(input('How old are you?: '))  # int('18') -> 18

if age >= 18:
    print('You are adult already.')
else:
    print('You are infant yet.')

# if <умова>
# після умови ставиться двокрапка
# після блоку if може бути нуль або більше блоків elif
# після if, elif, може бути один else

if age > 18:
    print('You are adult already.')
elif age == 18:
    print('age == 18')
else:
    print('You are infant yet.')



a = input('Введіть число: ')
a = int(a)
if a > 0:
    print('Число додатнє')
elif a == 0:
    print('a == 0')
else:
    print("Число від'ємне")



a = input('Введіть число: ')
a = int(a)
if a > 0:   # 1
    print('Число додатнє')
else:
    print("Число від'ємне або нуль")

print('hello world')


# True(1), False(0)
# число 0 приводиться до False
money = 0
if money:
    print(f"You have {money} on your bank account")
else:
    print("You have no money and no debts")

# None приводиться до False
result = None
if result:
    print(result)
else:
    print('Result is None, do something')

# пустий контейнер приводиться до False(рядок, список, кортеж, множина)
user_name = input('Enter your name: ')

if user_name:
    print(f'Hello, {user_name}')
else:
    print('Hi, Anonym!')


# булева алгебра
name = 'Taras'
age = 18
has_driver_license = True

if name and age >= 18 and has_driver_license:   # True and True and True
    print(f'User {name} can rent a car')
else:
    print("User can't rent a car")


# and(І) -> вираз виконається якщо обидві умови виконаються
# A       B        A and B
# True   True       True
# True   False      False
# False  True       False
# False  False      False


# or(АБО) -> вираз виконається якщо хоча б одна умова виконалась  +
# A       B        A or B
# True   True       True
# True   False      True
# False  True       True
# False  False      False


# not(Ні) -> заперечення
# A      not A
# True   False
# False  True


is_nice = True
state = 'nice' if is_nice else 'not nice'

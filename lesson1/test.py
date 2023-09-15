# None - пустота
# Числа - integer(цілі числа), float(дробові числа)
# Boolean - логічний тип(Правда або брехня) True or False
# Рядки - текст

a = None


b = 3.9
c = 10
name = 'Sasha'
print(name[2])
s = 'Hello world!'

s1 = 'Hello'
s2 = 'world'
print(s1 + s2)

# True(1), False(0)
a = False
b = True

age = 18
adult1 = age >= 18  # True
print(adult1)


age = 15
adult2 = age >= 18
print(adult2)

print(0.1 + 0.2 == 0.3)
# 0.1 + 0.2 = 0.3
print(0.1 + 0.2)  # 0.30000000000004
# 1 -> 01
# 2 -> 10
# 3 -> 11
# 4 -> 100
# 5 -> 101
number = int(input("Введіть число: ")) # функція input повертає рядкове представлення input("Введіть число: ") -> '10'
print(type(number))
print(number + 10)
# str -> string -> рядок
# 10 -> "10" -> 10
# '' ""
print('В\'ячеслав')  # \' -> апостроф, а не закриття рядка

# int('10') -> 10
# str, int, float, bool
true_or_false = input('Введіть правду чи брехню, якщо це брехня то нічого не вводьте, якщо це правда, то будь-що: ')
true_or_false = bool(true_or_false)
print(true_or_false)  # 


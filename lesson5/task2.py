# На собеседованиях часто любят спрашивать про алгоритмы. Например, рассчитайте наибольший
# общий делитель (НОД) двух положительных чисел. НОД — это наибольшее число, на которое без
# остатка делятся оба числа.
#
# Есть несколько алгоритмов для нахождения НОД, но мы разберем циклический алгоритм
#
# Пусть заданы два числа first и second.
# Выберем меньшее из них и присвоим переменной gcd.
# Пока first или second не делятся на gcd без остатка, выполнять цикл, где уменьшаем переменную
# gcd на единицу.
# Когда цикл закончится в переменной gcd будет НОД для first и second
# Напишите программу, которая для двух положительных целых чисел находит НОД.
#
# Примечание: Для условия цикла в пункте 3 необходимо помнить, что цикл while выполняется при
# условии True, а наш цикл должен закончиться, только если gcd разделил оба числа без остатка.
# 10, 5
# gcd = 5
first = int(input("Enter the first integer: "))
second = int(input("Enter the second integer: "))

gsd = first if first < second else second
while first % gsd or second % gsd:
    gsd -= 1

print(gsd)
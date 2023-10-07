x = int(input('x: '))
y = int(input('y: '))

if x >= 0:
    if y >= 0:
        print('Перша чверть')
    else:
        print('Четверта чверть')
else:
    if y >= 0:
        print('Друга чверть')
    else:
        print('Третя чверть')

# > 1, 2, 3, 4, 5, 6, 7
# == 0
# < -1, -2, -3, -4, -5
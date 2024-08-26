first = input('Введите целые числа: ')
second = input('Введите целые числа: ')
third = input('Введите целые числа: 1')
if first == second and second == third:
    print(3)
elif first == second or second == third:
    print(2)
else:
    print(0)

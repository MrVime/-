first = int(input('Введите целые числа: '))
second = int(input('Введите целые числа: '))
third = int(input('Введите целые числа: '))
if first == second and second == third:
    print(3)
elif first == second or second == third or first == third:
    print(2)
else:
    print(0)

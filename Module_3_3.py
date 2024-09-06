# 1.Функция с параметрами по умолчанию:
def print_params(a=1, b='строка', c=True):
    print(a, b, c, '\n')


print_params(b=25)
print_params(c=[1, 2, 3])

# 2.Распаковка параметров:
values_list = [516, 'UvU', False]
values_dict = {'a': 'O_O', 'b': None, 'c': 305}
print_params(*values_list)
print_params(**values_dict)

# 3.Распаковка + отдельные параметры:
values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
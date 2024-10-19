def calculate_structure_sum(list1):
    temporary_variable = 0
    if type(list1) == int:
        temporary_variable += list1
    elif type(list1) == str:
        temporary_variable += len(list(list1))
    elif type(list1) == list or type(list1) == tuple or type(list1) == set:
        temporary_variable += the_amount_the_list(list1)
    elif type(list1) == dict:
        temporary_variable += the_amount_the_dict(list1)
    return temporary_variable


def the_amount_the_dict(dict1):
    sum_dict = 0
    for i in dict1:
        sum_dict += calculate_structure_sum(i)
        sum_dict += calculate_structure_sum(dict1[i])
    return sum_dict


def the_amount_the_list(list1_or_tuple):
    sum_list = 0
    for i in list1_or_tuple:
        sum_list += calculate_structure_sum(i)
    return sum_list


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)

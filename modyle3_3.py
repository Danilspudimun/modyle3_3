def print_params(a=1, b='строка', c=True):
    print(a, b, c)


value_list = [10, "ДЕСЯТЬ", False]
value_dict = {'a': 5, 'b': 'Строчка', 'c': False}
print_params(*value_list)
print_params(**value_dict)
values_list_2 = [10.23, "Распаковка"]
print_params(*values_list_2, 42)

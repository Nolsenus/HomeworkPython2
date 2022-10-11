# Параметр do_crosses_count_ащк_фдд нужен для того, чтобы уточнить может ли
# один и тот же символ быть частью разных вхождений.
# Например: строки "ааа" и "аа" - можно сказать что "аа" входит в "ааа" 2 раза ("[аа]а" и "а[аа]"),
# а можно сказать, что только 1 раз, так как второй символ уже использовался в первом вхождении.
def num_of_entrances(string, search, do_crosses_count_for_all=True):
    # Считаем, что пустая строка может содержаться только в пустой строке
    if string == '' and search == '':
        return 1
    if string == '' or search == '':
        return 0
    if len(search) > len(string):
        temp = search
        search = string
        string = temp
    if do_crosses_count_for_all:
        return helper_cross_counts_for_all(string, search)
    return helper_cross_counts_once(string, search)


# Вариант, где "аа" втречается в "ааа" 2 раза
def helper_cross_counts_for_all(string, search):
    result = 0
    i = 0
    while i < len(string):
        if string[i] == search[0]:
            j = 0
            i_copy = i
            while i_copy < len(string) and j < len(search) and string[i_copy] == search[j]:
                i_copy += 1
                j += 1
            if j == len(search):
                result += 1
        i += 1
    return result


# Вариант, где "аа" встречается в "ааа" 1 раз
def helper_cross_counts_once(string, search):
    result = 0
    i = 0
    while i < len(string):
        if string[i] == search[0]:
            j = 0
            while i < len(string) and j < len(search) and string[i] == search[j]:
                i += 1
                j += 1
            if j == len(search):
                result += 1
        else:
            i += 1
    return result


a = input('Введите первую строку: ')
b = input('Введите вторую строку: ')
print('Может ли один символ относиться к разным вхождениям?')
c = input('Если да, напишите "Да", если нет напишите что-либо кроме "Да": ')
print(f'{a}, {b}, ', end='')
if c == "Да":
    print(f'Один сивол может относиться к разным вхождениям -> {num_of_entrances(a, b)}')
else:
    print(f'Один символ не может относиться к разным вхождениям -> {num_of_entrances(a, b, False)}')


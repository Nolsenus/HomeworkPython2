import decimal
from decimal import Decimal


def sum_of_digits(n):
    if n < 0:
        n = -n
    result = 0
    before_point = n // 1
    after_point = n % 1
    while before_point > 0:
        result += before_point % 10
        before_point //= 10
    while after_point % 1 > 0:
        after_point *= 10
        result += (after_point % 10) // 1
    return result


try:
    a = Decimal(input('Введите число: '))
    print(f'{a} -> {sum_of_digits(a)}')
except decimal.InvalidOperation:
    print('Вы ввели не число.')

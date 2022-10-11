def multiply_all_up_to(n):
    result = [1]
    for i in range(2, n + 1):
        result.append(i * result[i - 2])
    return result


try:
    n = int(input('Введите целое положительное число: '))
    if n < 1:
        print("Вы ввели не положительное число.")
    else:
        print(f'{n} -> {multiply_all_up_to(n)}')
except ValueError:
    print('Вы ввели не целое число.')

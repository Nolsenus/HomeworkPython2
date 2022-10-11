import random
import time


def test_case(values):
    first_clause = False
    second_clause = True
    for i in values:
        first_clause = first_clause or i
        second_clause = second_clause and not i
    first_clause = not first_clause
    return first_clause is second_clause


true_false = [True, False]
count = random.randint(5, 25)
predicates = []
all_true = True
start = time.perf_counter()
for i in range(100):
    print(f'Проход номер {i + 1}')
    for j in range(2 ** count):
        for k in range(count):
            predicates.append(true_false[j % 2])
            j //= 2
        test = test_case(predicates)
        # print(f'{predicates} -> {test}')
        if not test:
            all_true = False
            print(f'Проход номер {i}, {predicates} - Высказывание оказалось ложно!')
            break
        predicates.clear()
    if not all_true:
        break
end = time.perf_counter()
print(f'Количество предикат: {count} -> время работы {end - start}')

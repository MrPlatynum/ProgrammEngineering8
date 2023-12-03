#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


if __name__ == '__main__':
    numbers = tuple(map(int, input("Введите кортеж целых чисел через пробел: ").split()))

    # Проверить количество элементов кортежа.
    if len(numbers) < 2:
        print("Кортеж должен содержать как минимум два элемента", file=sys.stderr)
        exit(1)

    found = False
    for i, num in enumerate(numbers[:-1]):
        if num % 2 != 0 and numbers[i + 1] % 2 != 0:
            print(f"Первая пара соседних нечетных чисел найдена в позициях {i} и {i + 1}")
            found = True
            break

    # Вывод результата, если пара не найдена.
    if not found:
        print("В кортеже нет соседних нечетных чисел")

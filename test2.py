"""
2. Написать функцию, которая принимает на вход два
 целых числа (минимум и максимум) и возвращает список
  всех простых чисел в заданном диапазоне.
"""
from typing import *


"""
первый способ (медленный)
"""


def is_prime(x: int) -> bool:
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


def prime_number_generator1(x_min, x_max: int) -> List[int]:
    return [i for i in range(x_min, x_max + 1) if is_prime(i)]


"""
второй способ (медленный)
"""


def prime_number_generator2(x_min, x_max: int) -> List[int]:
    prime_numbers = []
    for x in range(x_min, x_max + 1):
        j = 0
        i = 2
        while i*i <= x and j != 1:
            if x % i == 0:
                j = 1
            i += 1
        if j == 1:
            prime_numbers.append(x)
    return prime_numbers


"""
третий способ (быстрый)
"""


def prime_numbers_generator3(x_min, x_max: int) -> List[int]:
    prime_numbers = []
    is_prime_numbers = [True for i in range(x_max + 1)]
    i = 2
    while i*i <= x_max:
        if is_prime_numbers[i]:
            for j in range(i * i, x_max + 1, i):
                is_prime_numbers[j] = False
        i += 1
    for i in range(x_min, x_max + 1):
        if is_prime_numbers[i]:
            prime_numbers.append(i)
    return prime_numbers

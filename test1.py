""""
1. Написать функцию, которая принимает на вход список целых
 чисел и возвращает новый список, содержащий только уникальные
 элементы из исходного списка.
"""
from typing import *


def unique_list_1(lst: List[int]) -> List[int]:
    return list(set(lst))


def unique_list_2(lst: List[int]) -> List[int]:
    new_lst = []
    for i in range(len(lst)):
        if lst[i] not in new_lst:
            new_lst.append(lst[i])
    return new_lst


def unique_list_3(lst: List[int]) -> List[int]:
    return [x for num, x in enumerate(lst) if x not in lst[:num]]

"""
4. Написать программу, которая сортирует список строк по длине,
 сначала по возрастанию, а затем по убыванию.
"""
import typing


lines_list = ['строка довольно длинная, но не самая',
              'самая длинная строка из всех строк в этом списке',
              'строка покороче довольно длинной',
              'самая короткая строка',]


def sort_lines(lines_list: typing.List[str], reverse=False) -> typing.List[str]:
    return sorted(lines_list, key=len, reverse=reverse)


print(sort_lines(lines_list))
print(sort_lines(lines_list, reverse=True))

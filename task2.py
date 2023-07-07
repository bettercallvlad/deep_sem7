# ### Задача 2
#
# Напишите функцию, которая генерирует псевдоимена.
# Имя должно начинаться с заглавной буквы, состоять из 4-7 букв,
# среди которых обязательно должны быть гласные.
# Полученные имена сохраните в файл.
from random import choice, randint

VOVELS = 'euioay'
CONSONANTS = 'wrtpsdfghklzcvnmb'


def fill_file_names(rows: int, filename: str):
    with open(filename, 'w') as file:
        for _ in range(rows):
            print(generate_name(4, 7), file=file)


def generate_name(start, stop) -> str:
    return ''.join([choice(choice([VOVELS, CONSONANTS]))
            for _ in range(randint(start, stop))]).capitalize()

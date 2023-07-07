"""Задача 4
Создайте функцию, которая создаёт файлы с указанным расширением.
Функция принимает следующие параметры: расширение

минимальная длина случайно сгенерированного имени, по умолчанию 6
максимальная длина случайно сгенерированного имени, по умолчанию 30
минимальное число случайных байт, записанных в файл, по умолчанию 256
максимальное число случайных байт, записанных в файл, по умолчанию 4096
количество файлов, по умолчанию 42
Имя файла и его размер должны быть в рамках переданного диапазона.

Задача 5
Доработаем предыдущую задачу. Создайте новую функцию которая генерирует
файлы с разными расширениями. Расширения и количество файлов функция
принимает в качестве параметров. Количество переданных расширений может
быть любым. Количество файлов для каждого расширения различно.
 Внутри используйте вызов функции из прошлой задачи.
"""

from task2 import generate_name
from random import randint, choice
from os import mkdir


def gen_random_files(min_len_name: int = 6,
                     max_len_name: int = 30,
                     min_count_bytes: int = 256,
                     max_count_bytes: int = 4096,
                     files_count: int = 42,
                     extensions: list[str] = None,
                     path: str = 'files_for_task4'):

    for _ in range(files_count):
        extension = choice(extensions)
        filename = generate_name(min_len_name, max_len_name)
        try:
            write_to_file(path, filename,
                          extension,
                          min_count_bytes, max_count_bytes)
        except FileNotFoundError:
            mkdir(path)
            write_to_file(path, filename,
                          extension,
                          min_count_bytes, max_count_bytes)


def gen_random_files_with_extensions(extensions: list[str],
                                     num_files: int,
                                     path: str = 'files_for_task4'):
    gen_random_files(
        extensions=extensions,
        files_count=num_files,
        path=path
    )


def write_to_file(path,
                  filename,
                  extension,
                  min_count_bytes,
                  max_count_bytes):
    with open(f'{path}/{filename + extension}', 'w') as file:
        data = bytes(randint(1, 255) for _ in range(randint(min_count_bytes,
                                                            max_count_bytes)))
        file.write(str(data))


gen_random_files_with_extensions(
    extensions=['.txt', '.md', '.csv', '.json'],
    num_files=12
)

"""Задача 7
Создайте функцию для сортировки файлов по директориям в зависимости
от расширения. Каждая группа включает файлы с
несколькими расширениями.
В исходной папке должны остаться только те файлы, которые не подошли для сортировки."""
from os import listdir, mkdir, chdir, replace
from pathlib import Path


def get_exts(exts: list[str]) -> list[str]:
    exts = set(map(lambda x: x.split('.')[-1], exts))
    return list(exts)


def sort_files(working_dir: str = 'files_for_task4'):
    exts = get_exts(listdir(Path(working_dir)))
    chdir(Path(working_dir))
    for ext in exts:
        try:
            mkdir(ext)
        except FileExistsError:
            pass
    for file in filter(lambda x: x.find('.') != -1, listdir()):
        prev = Path(file)
        prev.replace(Path.cwd() / file.split('.')[-1] / prev)


sort_files()

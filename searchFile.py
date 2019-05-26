import os
# библиотека typing (типы)
from typing import List
from searchDirectory import searchDirectory

#l: List[str] = [] запист с типизацией.

# контейнер list
l = []
# функция - обход директории с глубокой рекурсией на поиск .pdf
def dirLoop():
    # вызов функции (выбор директории)
    directory = searchDirectory()
    # рекурсивный обход директории на поиск файлов .pdf
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".pdf"):
                # добавление в контейнер list ИМЕНИ найденного файла
                l.append([(os.path.join(file)), root])
    return l

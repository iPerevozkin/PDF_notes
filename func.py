from  tkinter import *
import os
from tkinter import filedialog
#######################################################
# функция выбора директории и записи её в переменную
def searchDirectory():
    directory = filedialog.askdirectory()
    handle = open('directory.txt', 'w')
    handle.write(directory)
    handle.close()
    pass



# функция - обход директории с глубокой рекурсией на поиск .pdf
def dirLoop():
    # контейнер list
    directory = []
    handle = open('directory.txt', 'r')
    l = []
    for line in handle.readlines():
        directory.append(line)
    handle.close()
    print(directory)
    # рекурсивный обход директории на поиск файлов .pdf
    for root, dirs, files in os.walk(directory[0]):
        for file in files:
            if file.endswith(".pdf"):
                # добавление в контейнер list ИМЕНИ найденного файла
                l.append([(os.path.join(file)), root])
    return l

#############################################################################

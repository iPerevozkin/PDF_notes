import os
from tkinter import filedialog, END
#######################################################


# функция открытия файлов в LISTBOX
def open(directory, massivData, listbox1):
    massivData.clear()
    listbox1.delete(0, 'end')
    massivData.extend(dirLoop(directory))
    addBox(massivData, listbox1)


# функция выбора пути
def searchDirectory(directory, textDir):
     textDir.delete(1.0, END)
     directory.clear()
     directory.insert(0, filedialog.askdirectory())
     textDir.insert(1.0, directory)


# функция - обход директории с глубокой рекурсией на поиск .pdf
def dirLoop(directory):
    massiv = []
    for root, dirs, files in os.walk(directory[0]):
        for file in files:
            if file.endswith(".pdf"):
                # добавление в контейнер list ИМЕНИ найденного файла
                massiv.append([(os.path.join(file)), root])
    return massiv


# функция запуска выбранного файла
def fileOpen(listbox1, massivData):
    # индекс выделенного файла listbox (список) curselection функция
    sel = list(listbox1.curselection())
    ''' читает дирикторию с файлами и делает кортеж из списка произведений [0],
     [1] - полный путь до папки'''
    os.startfile(os.path.join(massivData[sel[0]][1], massivData[sel[0]][0]))
# добавление списка в LIstbox


def addBox(massivData, listbox1):
    for i in massivData:
        listbox1.insert(0, i[0])
    return listbox1

###############################################################

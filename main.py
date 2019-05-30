# импорт Tkinter
from tkinter import *
# функция dir_loop (перебирает файлы в указанной директории)
from func import dirLoop, searchDirectory
# библиотека системы
import os
#################################################################################
listing = dirLoop()
#################################################################################
# функция запускающая dirLoop -> searchDirectory, получает путь директории,
# потом парсит директории, добавляет список в listbox
def outListing():
    # читает дирикторию с файлами и делает кортеж из списка произведений [0], [1] - полный путь до папки
    directory = searchDirectory()
    for i in listing:
        listbox1.insert(END, i[0])
    pass

# функция запуска выбранного файла
def fileSelection():
    # индекс выделенного файла listbox (список) curselection функция
    selection = list(listbox1.curselection())
    # читает дирикторию с файлами и делает кортеж из списка произведений [0], [1] - полный путь до папки
    # запуск файла | selection - функция
    os.startfile(os.path.join(listing[selection[0]][1], listing[selection[0]][0]))

# Tkinter init
root = Tk()
# Title
root.title('PDF_reader')
# размер окна
root.geometry('800x600+200+100')
# init Frame
frame = Frame()
frame.pack(side = BOTTOM, expand = True)
# лист списка
listbox1 = Listbox(root, height=35, width=70)
listbox1.pack(side = LEFT)
# текст пути
textDir = Text(frame, height=1, width=21, font='Arial 15 bold')
textDir.pack(side=LEFT)


# init всех Button
button1 = Button(frame, text="Open file", width=50, command=fileSelection)
button1.pack(pady = 5)
button2 = Button(frame, text="Search", width=50)
button2.pack(pady = 5)
button3 = Button(frame, text="Open directory", width=50, command=outListing)
button3.pack(pady = 5)
button4 = Button(frame, text="Add", width=50)
button4.pack(pady = 5)
button5 = Button(frame, text="big", width=50)
button5.pack(pady = 5)
button6 = Button(frame, text="class", width=50)
button6.pack(pady = 5)
button7 = Button(frame, text="Add", width=50)
button7.pack(pady = 5)
button8 = Button(frame, text="Add", width=50)
button8.pack(pady = 5)

root.mainloop()

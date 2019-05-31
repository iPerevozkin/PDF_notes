# импорт Tkinter
from tkinter import *
# функция dir_loop (перебирает файлы в указанной директории)
from func import dirLoop, searchDirectory
# библиотека системы
from os import startfile, path
##############################################################################

##############################################################################
# функция запускающая dirLoop -> searchDirectory, получает путь директории,
# потом парсит директории, добавляет список в listbox


def outListing():
    directory = searchDirectory()
    listing = dirLoop()
    for i in listing:
        listbox1.insert(END, i[0])
    pass


# функция запуска выбранного файла
def fileSelection():
    # индекс выделенного файла listbox (список) curselection функция
    selection = list(listbox1.curselection())
    ''' читает дирикторию с файлами и делает кортеж из списка произведений [0],
     [1] - полный путь до папки
    запуск файла | selection - функция'''
    startfile(path.join(listing[selection[0]][1], listing[selection[0]][0]))

# Tkinter init
root = Tk()
# Title
root.title('PDF_reader')
# размер окна
root.geometry('900x600+200+100')
# init Frame
#frame = Frame()
#frame.grid(side = BOTTOM, expand = True)
# лист списка
listbox1 = Listbox(root, height=60, width=140)
listbox1.grid(row=1, column=0, rowspan=4, columnspan=5, padx=30)
# текст пути
textDir = Text(height=1, width=21, font='Arial 15 bold')
textDir.grid(row=0, column=1)


# init всех Button
button1 = Button(text="Open file", width=50, command=fileSelection)
button1.grid()
button2 = Button(text="output")
button2.grid(row=0, column=4, pady=10, padx=10)
button3 = Button(text="directory selection", command=outListing)
button3.grid(row=0, column=0, pady=10, padx=10)
button4 = Button(text="Add", width=50)
button4.grid()
button5 = Button(text="big", width=50)
button5.grid()
button6 = Button(text="class", width=50)
button6.grid()
button7 = Button(text="Add", width=50)
button7.grid()
button8 = Button(text="Add", width=50)
button8.grid()

root.mainloop()

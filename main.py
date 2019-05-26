# импорт файлов ########################

# импорт Tkinter
from tkinter import *
# функция dir_loop (перебирает файлы в указанной директории)
from searchFile import dirLoop
# библиотека системы
import os

from runFileSelection import fileSelection

# Tkinter init
root = Tk()
# init Frame
frame = LabelFrame(text = 'функции', relief = FLAT)
frame_Button_categoty = LabelFrame(text = 'категории', relief = FLAT)

# Title
root.title('PDF_reader')
# размер окна
root.geometry('800x600+200+100')


# лист списка
listbox1 = Listbox(root, height=35, width=70)

# добавляет в лист бокс весь список из listing --> из переменной DIR_LOOP
def outListing():
    # читает дирикторию с файлами и делает кортеж из списка произведений [0], [1] - полный путь до папки
    listing = dirLoop()
    for i in listing:
        listbox1.insert(END, i[0])
    return listbox1


# init всех Button
# Button open c функцией
button1 = Button(frame, text="Open file", width=50, command=fileSelection)
button2 = Button(frame, text="Search", width=50)
button3 = Button(frame, text="Open directory", width=50, command=outListing)
button4 = Button(frame, text="Add", width=50)

button5 = Button(frame_Button_categoty, text="big", width=50)
button6 = Button(frame_Button_categoty, text="class", width=50)
button7 = Button(frame_Button_categoty, text="Add", width=50)
button8 = Button(frame_Button_categoty, text="Add", width=50)


# пакует все виджеты
listbox1.pack(side = LEFT)

frame.pack(side = BOTTOM, expand = True)
frame_Button_categoty.pack(side = TOP, pady = 5)



button1.pack(pady = 5)
button2.pack(pady = 5)
button3.pack(pady = 5)
button4.pack(pady = 5)
button5.pack(pady = 5)
button6.pack(pady = 5)
button7.pack(pady = 5)
button8.pack(pady = 5)

root.mainloop()

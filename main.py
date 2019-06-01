# импорт Tkinter
import tkinter as tk
# три функции ВЫБОР ДИРЕКТОРИИ, ОТКРЫТИЕ СПИСКА ФАЙЛОВ, ОТКРЫТИЕ ФАЙЛА
from func import searchDirectory, open, fileOpen
##############################################################################
''' переменные в которых хранятся переменные
DIRECTORY - выбранный путь, MASSIVDATA - список файлов.'''

directory = ['путь до файла']
massivData = []
##############################################################################
# Tkinter init
root = tk.Tk()
# Title
root.title('PDF_reader')
# размер окна
root.geometry('900x600+200+100')
# лист списка
listbox1 = tk.Listbox(root, height=20, width=75, font='Arial 15')
listbox1.grid(row=1, column=0, rowspan=4, columnspan=5, padx=30)
# текст пути
textDir = tk.Text(height=1, width=35, font='Arial 15')
textDir.grid(row=0, column=2)
textDir.insert(1.0, directory)

# init всех Button
button1 = tk.Button(text="Open file", command= lambda: fileOpen(listbox1, massivData))
button1.grid(pady=10, padx=10)
button2 = tk.Button(text="open", command= lambda: open(directory, massivData, listbox1))
button2.grid(row=0, column=1, pady=10, padx=0)
button3 = tk.Button(text="dir selection", command= lambda: searchDirectory(directory, textDir))
button3.grid(row=0, column=0)

root.tk.mainloop()

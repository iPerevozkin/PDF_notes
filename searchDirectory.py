from  tkinter import *
from tkinter import filedialog
# функция выбора директории и записи её в переменную
def searchDirectory():
    directory = filedialog.askdirectory()
    return directory

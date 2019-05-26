# функция запуска выбранного файла
def fileSelection():
    # индекс выделенного файла listbox (список) curselection функция
    selection = list(listbox1.curselection())
    # запуск файла | selection - функция
    os.startfile(os.path.join(listing[selection[0]][1], listing[selection[0]][0]))

import tkinter as tk
from Program import itt
from tkinter import messagebox


def schedule(year, month, date):
    win = tk.Tk()
    win.title(str(year) + '年' + str(month) + '月' + str(date) + '日')
    win.geometry('1000x700')
    win.resizable(True, True)

    day = str(year) + str(month) + str(date)
    frame = tk.LabelFrame(win, text='代辦事項', padx=10, pady=10)
    listbox = tk.Listbox(frame)
    if itt.getIttValue(day) != 0:

        for i in itt.getIttValue(day):
            listbox.insert(tk.END, i)
    listbox.pack()
    menubar = tk.Menu(win)
    menubar.add_command(label="新增代辦事項", command=lambda: newSchedule(listbox, win, day))

    menubar.add_command(label="刪除代辦事項", command=lambda: askDelete(listbox, day))

    win.config(menu=menubar)

    frame.pack()
    win.mainloop()


def newSchedule(listbox, window, day):
    win = tk.Tk()
    win.title('新增代辦事項')
    win.geometry('500x300')
    win.resizable(True, True)

    input = tk.Entry(win)
    input.pack()
    tk.Button(win, text='新增', command=lambda: add(listbox, input.get(), day, win, window)).pack()


def add(listbox, text, day, win, window):
    listbox.insert(tk.END, text)
    itt.add(day, str(text))
    win.destroy()
    window.destroy()


def askDelete(listbox, year):
    result = messagebox.askyesno('提示', '確定要刪除嗎')
    if result:
        delete(listbox, year)


def delete(listbox, year):
    n, = listbox.curselection()
    listbox.delete(n)

    itt.delete(year, n)

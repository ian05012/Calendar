import tkinter as tk
import calendar as cal
import datetime
from Program import buttonExecute
from tkinter import messagebox
from Program import itt


def initial(year, month):
    window = tk.Tk()

    window.title('行事曆')
    window.geometry('1500x900')
    window.resizable(True, True)

    menubar = tk.Menu(window)
    menubar.add_command(label="下個月", command=lambda: nextMonth(window, year, month))
    menubar.add_command(label="上個月", command=lambda: lastMonth(window, year, month))
    menubar.add_command(label="跳至特定月份", command=lambda: input(window))

    window.config(menu=menubar)
    frame = tk.LabelFrame(window, text=str(month) + '月', padx=10, pady=10)
    week = ['Mon.', 'Tue.', 'Wed', 'Thu.', 'Fri', 'Sat.', 'Sun.']
    for day in range(0, 7):
        tk.Label(frame,
                 text=week[day],
                 width=12,
                 height=3,
                 font=100
                 ).grid(column=day, row=0)
    count = 1

    for i in range(1, 7):
        for j in range(0, 7):

            if count == 1 and firstDay(int(year), int(month)) != j:
                continue
            if count > int(cal.monthrange(year, month)[1]):
                break
            setButton(frame, year, month, count).grid(column=j, row=i)
            count += 1

    frame.pack()

    window.mainloop()


def setButton(frame, year, month, date):
    btn = tk.Button(
        frame,
        text=date,
        width=20,
        height=5,
        bg='white',
        command=lambda: buttonExecute.execute(year, month, date))

    if (year == datetime.datetime.today().year) and \
            (month == int(datetime.datetime.today().month)) and \
            (date == datetime.datetime.today().day):
        btn = tk.Button(
            frame,
            text=date,
            width=20,
            height=5,
            bg='yellow',
            command=lambda: buttonExecute.execute(year, month, date))

    string = str(year) + str(int(month)) + str(date)
    if itt.itt.__contains__(string):
        btn = tk.Button(
            frame,
            text=date,
            width=20,
            height=5,
            bg='#97CBFF',
            command=lambda: buttonExecute.execute(year, month, date))
    return btn


def firstDay(year, month):
    return int(cal.weekday(year, month, 1))


def nextMonth(window, year, month):
    month += 1
    if month > 12:
        month = 1
        year += 1
    window.destroy()
    initial(year, month)


def lastMonth(window, year, month):
    month -= 1
    if month < 1:
        month = 12
        year -= 1
    window.destroy()
    initial(year, month)


def input(window):
    win = tk.Tk()
    win.title('跳至特定月份')
    win.geometry('160x100')
    win.resizable(True, True)
    frame = tk.Frame(win)
    frame.pack()
    yearLable = tk.Label(frame, text='年份')
    yearInput = tk.Entry(frame, width=10)

    monthLable = tk.Label(frame, text='月份')
    monthInput = tk.Entry(frame, width=10)

    yearLable.grid(column=0, row=0)
    yearInput.grid(column=0, row=1)
    monthLable.grid(column=1, row=0)
    monthInput.grid(column=1, row=1)

    btn = tk.Button(win, text='跳轉', command=lambda: jump(window, win, yearInput.get(), monthInput.get()))
    btn.pack()
    win.mainloop()


def jump(window, win, year, month):
    if not str.isdigit(year) or not str.isdigit(month):
        messagebox.showwarning('警告', '輸入錯誤')
        return
    if int(year) <= 0 or int(month) < 1 or int(month) > 12:
        messagebox.showwarning('警告', '輸入錯誤')
        return
    win.destroy()
    window.destroy()
    initial(int(year), int(month))

import tkinter as tk


def initial():
    window = tk.Tk()
    window.title('行事曆')
    window.geometry('1500x900')
    window.resizable(True, True)

    test = tk.Button(text="測試", activebackground='blue', activeforeground='yellow' )

    test.pack(side="top")
    window.mainloop()

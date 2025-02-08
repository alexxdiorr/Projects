import tkinter as tk
from tkinter import messagebox
import os

if not os.path.exists("Tasks.txt"):
    with open("Tasks.txt", "w", encoding="utf-8") as file:
        file.write("")

def addtask():
    value = EnterText.get().lower()
    d = {}
    with open('Tasks.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, val = line.split(':')
                d[key] = val
    if value != '' and value not in d:
        with open('Tasks.txt', 'a+', encoding='utf-8') as file:
            file.write(f"{value}:not finished\n")
        tk.messagebox.showinfo("Task added!", ('Task added successfully!'))
    else:
        tk.messagebox.showinfo("Error", ('Task field empty or item already exists.'))
    EnterText.delete(0, 'end')

def showtasks():
    with open('Tasks.txt', 'r+') as file:
        tk.messagebox.showinfo("Here are your tasks", (file.read()))

def cleartasks():
    with open('Tasks.txt', 'r+') as file:
        file.truncate(0)
    tk.messagebox.showinfo("To-do list cleared!", ('Your to-do list is now clear'))

def finishtask():
    value = EnterText.get().lower()
    d = {}
    with open('Tasks.txt', 'r') as file:
        for line in file:
            line = line.strip()
            if line:
                key, val = line.split(':')
                d[key] = val
    if value in d:
        d[value] = 'finished'
        tk.messagebox.showinfo("Task finished!", ('Task finished successfully!'))
    else:
        tk.messagebox.showinfo("Error", ('No such task has been found!'))
    with open('Tasks.txt', 'w') as file:
        for key, val in d.items():
            file.write(f"{key}:{val}\n")
    EnterText.delete(0, 'end')

def UpClick(i):
    showtasks()
def EnterClick(i):
    addtask()
def CtrlClick(i):
    finishtask()
def TabClick(i):
    cleartasks()
def EscClick(i):
    window.quit()

window = tk.Tk() #виндоу это окно

window.resizable(width=False, height=False) #нельзя менять разрешение окна

window.title("To-do List") #дать название окну

window.geometry("720x360") #дать разрешение окну

window["bg"] = "black" #дать цвет фону

thelist =  tk.Label(window, text = "Enter new task", font = ("Arial Bold", 15), fg = "white", bg = "black") #tk.Label создаёт ярлык + параметры
thelist.place(x=290, y = 25) #размещение ярлыка в окне

EnterText = tk.Entry(fg = "black", width= 45) #создать вводную строку, цвет букв, ширина строки
EnterText.place(x=232, y=65)

showlist = tk.Button(window, text="Show tasks (Up)", command=showtasks, width=40, height=2, fg="black", bg="white")
showlist.place(x=225, y=100)

window.bind('<Up>', UpClick)

addtasks = tk.Button(window, text="Add task (Enter)", command=addtask, width=40, height=2, fg="black", bg="white")
addtasks.place(x=225, y=150)

window.bind('<Return>', EnterClick)

finishtasks = tk.Button(window, text="Finish task (Left Ctrl)", command=finishtask, width=40, height=2, fg="black", bg="white")
finishtasks.place(x=225, y=200)

window.bind('<Control_L>', CtrlClick)

clear = tk.Button(window, text="Clear tasks (Tab)", command=cleartasks, width=40, height=2, fg="black", bg="white")
clear.place(x=225, y=250)

window.bind('<Tab>', TabClick)

quitting = tk.Button(window, text="Quit (Esc)", command=window.destroy, width=40, height=2, fg="black", bg="white")
quitting.place(x=225, y=300)

window.bind('<Escape>', EscClick)


window.mainloop()
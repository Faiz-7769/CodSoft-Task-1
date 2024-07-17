from tkinter import *
import tkinter.messagebox as tmsg
import os

root = Tk()
root.geometry("544x355")
root.minsize(544, 355)
root.title("To-Do List")
root.wm_iconbitmap("todolist.png")


# Commands
def plus():
    tasks = task_entry.get()
    if tasks != "":
        llist.insert(END, tasks)
        task_entry.delete(0, END)
    else:
        tmsg.showwarning("Warning", "You must enter a task.")


def remove():
    selected = llist.curselection()
    if selected:
        llist.delete(selected[0])
    else:
        tmsg.showwarning("Warning", "You must select a task.")


def update():
    selected = llist.curselection()
    if selected:
        new_task = task_entry.get()
        if new_task != "":
            llist.delete(selected[0])
            llist.insert(selected[0], new_task)
            task_entry.delete(0, END)
        else:
            tmsg.showwarning("Warning", "You must enter a task.")
    else:
        tmsg.showwarning("Warning", "You must select a task to update.")


def clear():
    llist.delete(0, END)


def save_tasks():
    tasks = llist.get(0, END)
    with open("tasks.txt", "w") as f:
        for task in tasks:
            f.write(task + "\n")


def load_tasks():
    if os.path.exists("tasks.txt"):
        with open("tasks.txt", "r") as f:
            tasks = f.readlines()
            for task in tasks:
                llist.insert(END, task.strip())


# Load tasks on startup
load_tasks()

# Listbox
llist = Listbox(root, width=50, height=10, relief=SOLID)
llist.grid(row=2, column=0, padx=20, pady=5, columnspan=3)

# Label for GUI
label = Label(root, text="Welcome to To-Do List App")
label.grid(row=0, column=0, columnspan=3, pady=10)

# Add task frame
add = Frame(root, borderwidth=2, relief="sunken")
add.grid(row=3, column=0, columnspan=3, pady=10)

# Task label and entry
l1 = Label(add, text="Task:")
l1.grid(row=0, column=0, padx=5)
task = StringVar()
task_entry = Entry(add, textvariable=task)
task_entry.grid(row=0, column=1, padx=5)

# Button frame
f1 = Frame(root, borderwidth=2, relief="solid")
f1.grid(row=4, column=0, columnspan=3, pady=10)

# Add, Remove, Update, and Clear buttons
b1 = Button(f1, text="Add", command=plus)
b1.grid(row=0, column=0, padx=5)
b2 = Button(f1, text="Remove", command=remove)
b2.grid(row=0, column=1, padx=5)
b3 = Button(f1, text="Update", command=update)
b3.grid(row=0, column=2, padx=5)
b4 = Button(f1, text="Clear", command=clear)
b4.grid(row=0, column=3, padx=5)
b5 = Button(f1, text="Save", command=save_tasks)
b5.grid(row=0, column=4, padx=5)

root.mainloop()

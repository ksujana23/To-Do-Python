from tkinter import *
from tkinter import messagebox

# Create window
root = Tk()
root.title("To-Do List Application")
root.geometry("500x650")
root.config(bg="#EAF6F6")


# Load tasks from file
def load_tasks():
    try:
        file = open("tasks.txt", "r")
        tasks = file.read().splitlines()
        file.close()

        for task in tasks:
            listbox.insert(END, task)
    except:
        pass


# Save tasks to file
def save_tasks():
    file = open("tasks.txt", "w")
    tasks = listbox.get(0, END)

    for task in tasks:
        file.write(task + "\n")

    file.close()


# Add task
def add_task():
    task = entry.get()

    if task != "":
        listbox.insert(END, task)
        entry.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task")


# Delete selected task
def delete_task():
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        listbox.delete(index)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Select a task first")


# Clear all tasks
def clear_tasks():
    if listbox.size() > 0:
        listbox.delete(0, END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "No tasks to clear")


# Heading
label = Label(
    root,
    text="TO-DO LIST APPLICATION",
    font=("Arial", 20, "bold"),
    bg="#EAF6F6"
)
label.pack(pady=20)


# Entry box
entry = Entry(root, width=30, font=("Arial", 14))
entry.pack(pady=10)

# Press Enter key to add task
entry.bind("<Return>", lambda event: add_task())


# Buttons
add_button = Button(
    root,
    text="Add Task",
    font=("Arial", 12),
    width=15,
    command=add_task
)
add_button.pack(pady=8)

delete_button = Button(
    root,
    text="Delete Task",
    font=("Arial", 12),
    width=15,
    command=delete_task
)
delete_button.pack(pady=8)

clear_button = Button(
    root,
    text="Clear All",
    font=("Arial", 12),
    width=15,
    command=clear_tasks
)
clear_button.pack(pady=8)


# Frame for listbox + scrollbar
frame = Frame(root)
frame.pack(pady=20)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

listbox = Listbox(
    frame,
    width=35,
    height=12,
    font=("Arial", 14),
    yscrollcommand=scrollbar.set
)
listbox.pack(side=LEFT)

scrollbar.config(command=listbox.yview)


# Footer
footer = Label(
    root,
    text="Created by Sujana Kasarapu",
    font=("Arial", 10),
    bg="#EAF6F6"
)
footer.pack(side="bottom", pady=10)


# Load saved tasks
load_tasks()

# Run app
root.mainloop()
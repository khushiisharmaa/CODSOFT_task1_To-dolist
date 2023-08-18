from tkinter import *
from tkinter import messagebox

def add_task():
    new_task = task_entry.get()
    if new_task:
        tasks.append(new_task)
        update_task_list()
        task_entry.delete(0, END)

def remove_task():
    selected_task = task_listbox.get(ACTIVE)
    if selected_task:
        tasks.remove(selected_task)
        update_task_list()

def update_task():
    selected_task = task_listbox.get(ACTIVE)
    if selected_task:
        updated_task = updated_task_entry.get()
        if updated_task:
            index = tasks.index(selected_task)
            tasks[index] = updated_task
            update_task_list()

def update_task_list():
    task_listbox.delete(0, END)
    for task in tasks:
        task_listbox.insert(END, task)

def show_all_tasks():
    all_tasks = "\n".join(tasks)
    messagebox.showinfo("All Tasks", all_tasks)

tasks = []

root = Tk()
root.title("Task Manager")

instructions = Label(root, text="Manage your tasks:")
instructions.pack()

task_label = Label(root, text="New Task:")
task_label.pack()

task_entry = Entry(root)
task_entry.pack()

add_button = Button(root, text="Add Task", command=add_task)
add_button.pack()

task_listbox = Listbox(root)
task_listbox.pack()

remove_button = Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

update_label = Label(root, text="Updated Task:")
update_label.pack()

updated_task_entry = Entry(root)
updated_task_entry.pack()

update_button = Button(root, text="Update Task", command=update_task)
update_button.pack()

show_all_button = Button(root, text="Show All Tasks", command=show_all_tasks)
show_all_button.pack()

update_task_list()

exit_button = Button(root, text="Exit", command=root.quit)
exit_button.pack()

root.mainloop()


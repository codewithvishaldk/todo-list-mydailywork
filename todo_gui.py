import tkinter as tk
from tkinter import messagebox
from ttkbootstrap import Style 

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({'task': task, 'completed': False})

    def view_tasks(self):
        return self.tasks

    def update_task(self, index, new_task):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['task'] = new_task
        else:
            print("Invalid task number.")

    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks.pop(index)
        else:
            print("Invalid task number.")

    def mark_task_completed(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index]['completed'] = True
        else:
            print("Invalid task number.")

class TodoApp(tk.Tk):
    def __init__(self, todo_list):
        super().__init__()
        
        # Apply ttkbootstrap style
        self.style = Style(theme='darkly')

        self.todo_list = todo_list
        self.title("To-Do List Application")
        self.geometry("400x400")
        self.configure(bg=self.style.colors.bg)

        self.task_entry = tk.Entry(self, width=50, font=('Arial', 12))
        self.task_entry.pack(pady=10)

        self.add_task_button = tk.Button(self, text="Add Task", command=self.add_task, bg=self.style.colors.primary, fg='white', font=('Arial', 12))
        self.add_task_button.pack(pady=5)

        self.tasks_listbox = tk.Listbox(self, width=50, height=10, font=('Arial', 12))
        self.tasks_listbox.pack(pady=10)

        self.update_task_button = tk.Button(self, text="Update Task", command=self.update_task, bg=self.style.colors.warning, fg='white', font=('Arial', 12))
        self.update_task_button.pack(pady=5)

        self.delete_task_button = tk.Button(self, text="Delete Task", command=self.delete_task, bg=self.style.colors.danger, fg='white', font=('Arial', 12))
        self.delete_task_button.pack(pady=5)

        self.mark_completed_button = tk.Button(self, text="Mark as Completed", command=self.mark_task_completed, bg=self.style.colors.success, fg='white', font=('Arial', 12))
        self.mark_completed_button.pack(pady=5)

        self.refresh_tasks()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.todo_list.add_task(task)
            self.task_entry.delete(0, tk.END)
            self.refresh_tasks()

    def update_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            new_task = self.task_entry.get()
            if new_task:
                self.todo_list.update_task(selected_task_index[0], new_task)
                self.task_entry.delete(0, tk.END)
                self.refresh_tasks()

    def delete_task(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.todo_list.delete_task(selected_task_index[0])
            self.refresh_tasks()

    def mark_task_completed(self):
        selected_task_index = self.tasks_listbox.curselection()
        if selected_task_index:
            self.todo_list.mark_task_completed(selected_task_index[0])
            self.refresh_tasks()

    def refresh_tasks(self):
        self.tasks_listbox.delete(0, tk.END)
        for task in self.todo_list.view_tasks():
            status = "Done" if task['completed'] else "Not Done"
            self.tasks_listbox.insert(tk.END, f"{task['task']} - {status}")

if __name__ == "__main__":
    todo_list = TodoList()
    app = TodoApp(todo_list)
    app.mainloop()

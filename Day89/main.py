import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        self.tasks = []

        # Input field and Add button
        self.task_entry = tk.Entry(root, width=40, font=("Arial", 12))
        self.task_entry.pack(pady=10)

        self.add_button = tk.Button(root, text="Add Task", width=15, command=self.add_task)
        self.add_button.pack()

        # Listbox to show tasks
        self.task_listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE, font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        # Buttons for complete and delete
        self.complete_button = tk.Button(root, text="Mark as Completed", width=20, command=self.mark_completed)
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(root, text="Delete Task", width=20, command=self.delete_task)
        self.delete_button.pack(pady=5)

    def add_task(self):
        task = self.task_entry.get().strip()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def mark_completed(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            task_text = self.task_listbox.get(index)
            if not task_text.startswith("[Done] "):
                self.task_listbox.delete(index)
                self.task_listbox.insert(index, "[Done] " + task_text)
                self.task_listbox.itemconfig(index, {'fg': 'gray'})
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

    def delete_task(self):
        selected = self.task_listbox.curselection()
        if selected:
            index = selected[0]
            self.task_listbox.delete(index)
            del self.tasks[index]
        else:
            messagebox.showwarning("Selection Error", "Please select a task.")

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()

import tkinter as tk
import time

class DangerousWritingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Dangerous Writing App")
        self.root.geometry("600x400")

        self.text_area = tk.Text(root, font=("Arial", 14), wrap=tk.WORD)
        self.text_area.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

        self.status_label = tk.Label(root, text="Start writing... Don't stop!", font=("Arial", 12), fg="red")
        self.status_label.pack()

        self.last_keypress_time = time.time()
        self.timer_running = True

        # Bind key press
        self.text_area.bind("<Key>", self.reset_timer)

        # Start the inactivity check loop
        self.check_inactivity()

    def reset_timer(self, event=None):
        self.last_keypress_time = time.time()

    def check_inactivity(self):
        if self.timer_running:
            current_time = time.time()
            elapsed = current_time - self.last_keypress_time

            if elapsed >= 5:
                self.text_area.delete("1.0", tk.END)
                self.status_label.config(text="You stopped writing! Text deleted!", fg="black")
                self.last_keypress_time = current_time  # Reset timer after deletion

        self.root.after(1000, self.check_inactivity)  # Check every second

if __name__ == "__main__":
    root = tk.Tk()
    app = DangerousWritingApp(root)
    root.mainloop()

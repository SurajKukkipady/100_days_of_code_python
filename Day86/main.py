import tkinter as tk
import time
import random

# Sample texts to type
SAMPLE_TEXTS = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language loved by many developers.",
    "Typing speed is measured in words per minute.",
    "Practice daily to improve your typing accuracy and speed.",
    "Consistency and dedication are key to mastering any skill."
]

class TypingSpeedApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.start_time = None

        self.instructions = tk.Label(root, text="Type the text below as fast as you can:", font=("Arial", 14))
        self.instructions.pack(pady=10)

        self.text_display = tk.Label(root, text=self.sample_text, wraplength=500, font=("Arial", 12), bg="lightyellow", padx=10, pady=10)
        self.text_display.pack(pady=10)

        self.text_entry = tk.Text(root, height=5, width=60, font=("Arial", 12))
        self.text_entry.pack(pady=10)
        self.text_entry.bind("<KeyPress>", self.start_typing)

        self.result_label = tk.Label(root, text="", font=("Arial", 12))
        self.result_label.pack(pady=10)

        self.reset_button = tk.Button(root, text="Reset", command=self.reset_test)
        self.reset_button.pack(pady=10)

    def start_typing(self, event):
        if self.start_time is None:
            self.start_time = time.time()
            self.text_entry.bind("<Return>", self.calculate_results)

    def calculate_results(self, event):
        end_time = time.time()
        typed_text = self.text_entry.get("1.0", tk.END).strip()
        elapsed_time = end_time - self.start_time

        # Calculate WPM
        word_count = len(typed_text.split())
        wpm = round((word_count / elapsed_time) * 60)

        # Calculate accuracy
        correct_chars = sum(1 for i, c in enumerate(typed_text) if i < len(self.sample_text) and c == self.sample_text[i])
        accuracy = round((correct_chars / max(len(self.sample_text), 1)) * 100)

        self.result_label.config(text=f"WPM: {wpm} | Accuracy: {accuracy}%")
        self.text_entry.unbind("<KeyPress>")
        self.text_entry.unbind("<Return>")

        return "break"  # Prevent newline on Enter

    def reset_test(self):
        self.sample_text = random.choice(SAMPLE_TEXTS)
        self.text_display.config(text=self.sample_text)
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.text_entry.bind("<KeyPress>", self.start_typing)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedApp(root)
    root.mainloop()

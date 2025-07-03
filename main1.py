import tkinter as tk
from tkinter import messagebox
from time import time
from difflib import SequenceMatcher

# Sample text to type
sample_text = (
    "Python is a versatile programming language known for its readability and simplicity. "
    "It supports multiple programming paradigms, including object-oriented, procedural, and functional programming. "
    "With an extensive standard library and strong community support, Python is widely used in web development, data analysis, artificial intelligence, automation, and more. "
    "Indentation is a key feature that defines code blocks, making Python both powerful and beginner-friendly. "
    "Practice and consistency are essential to mastering Python programming."
)

class TypingTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")
        self.start_time = None

        # Sample Text Label
        self.label = tk.Label(root, text=sample_text, wraplength=500, font=("Helvetica", 14), justify="left")
        self.label.pack(pady=10)

        # Typing Area
        self.text_entry = tk.Text(root, height=5, width=60, font=("Helvetica", 14))
        self.text_entry.pack(pady=10)
        self.text_entry.bind('<KeyPress>', self.start_timer)
        self.text_entry.focus_set()  # Autofocus on start

        # Buttons
        button_frame = tk.Frame(root)
        button_frame.pack(pady=10)

        self.submit_btn = tk.Button(button_frame, text="Finish and Calculate", command=self.calculate_result)
        self.submit_btn.grid(row=0, column=0, padx=10)

        self.reset_btn = tk.Button(button_frame, text="Reset", command=self.reset_test)
        self.reset_btn.grid(row=0, column=1, padx=10)

        # Result Display
        self.result_label = tk.Label(root, text="", font=("Helvetica", 12), justify="left")
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:
            self.start_time = time()

    def calculate_result(self):
        if self.start_time is None:
            messagebox.showinfo("Info", "You haven't started typing yet!")
            return

        end_time = time()
        elapsed_time = (end_time - self.start_time) / 60  # in minutes

        user_text = self.text_entry.get("1.0", tk.END).strip()

        # WPM: Total words typed divided by time
        words_typed = len(user_text.split())
        wpm = round(words_typed / elapsed_time) if elapsed_time > 0 else 0

        # Accuracy using SequenceMatcher
        accuracy = round(SequenceMatcher(None, sample_text, user_text).ratio() * 100, 2)

        # Result display
        result = (
            f"WPM: {wpm}\n"
            f"Accuracy: {accuracy}%\n"
            f"Time Taken: {round(elapsed_time * 60, 2)} seconds"
        )
        self.result_label.config(text=result)

        self.start_time = None  # Reset timer after each calculation

    def reset_test(self):
        self.text_entry.delete("1.0", tk.END)
        self.result_label.config(text="")
        self.start_time = None
        self.text_entry.focus_set()

# Run the App
if __name__ == "__main__":
    root = tk.Tk()
    app = TypingTestApp(root)
    root.mainloop()

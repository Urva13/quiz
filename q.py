import random
import time
import tkinter as tk
from tkinter import messagebox

class Quiz:
    def __init__(self):
        self.questions = {
            "What is the capital of France?": {
                "A": "Paris",
                "B": "London",
                "C": "Berlin",
                "D": "Rome"
            },
            "What is the largest planet in our solar system?": {
                "A": "Earth",
                "B": "Saturn",
                "C": "Jupiter",
                "D": "Uranus"
            },
            "What is the smallest country in the world?": {
                "A": "Vatican City",
                "B": "Monaco",
                "C": "Nauru",
                "D": "Tuvalu"
            },
            "What is the largest living species of lizard?": {
                "A": "Komodo dragon",
                "B": "Saltwater crocodile",
                "C": "Black mamba",
                "D": "Green anaconda"
            },
            "What is the highest mountain peak in the solar system?": {
                "A": "Mount Everest",
                "B": "Olympus Mons",
                "C": "Mauna Kea",
                "D": "Denali"
            }
        }
        self.answers = {
            "What is the capital of France?": "A",
            "What is the largest planet in our solar system?": "C",
            "What is the smallest country in the world?": "A",
            "What is the largest living species of lizard?": "A",
            "What is the highest mountain peak in the solar system?": "B"
        }
        self.score = 0
        self.current_question = None
        self.time_left = 30

    def start_quiz(self):
        self.root = tk.Tk()
        self.root.title("Quiz")
        self.label = tk.Label(self.root, text="", wraplength=400)
        self.label.pack()
        self.entry = tk.Entry(self.root)
        self.entry.pack()
        self.button = tk.Button(self.root, text="Submit", command=self.check_answer)
        self.button.pack()
        self.timer_label = tk.Label(self.root, text="Time left: 30 seconds")
        self.timer_label.pack()
        self.next_question()
        self.root.after(1000, self.decrement_timer)
        self.root.mainloop()

    def next_question(self):
        self.questions_list = list(self.questions.keys())
        random.shuffle(self.questions_list)
        self.current_question = self.questions_list.pop()
        self.label.config(text=self.current_question)
        for option, answer in self.questions[self.current_question].items():
            self.label.config(text=self.label.cget("text") + "\n" + option + ": " + answer)
        self.entry.delete(0, tk.END)

    def check_answer(self):
        user_answer = self.entry.get().upper()
        if user_answer == self.answers[self.current_question]:
            self.score += 1
            messagebox.showinfo("Correct!", "Your answer is correct!")
        else:
            messagebox.showinfo("Incorrect", f"Sorry, the correct answer is {self.answers[self.current_question]}")
        self.next_question()

    def decrement_timer(self):
        self.time_left -= 1
        self.timer_label.config(text=f"Time left: {self.time_left} seconds")
        if self.time_left > 0:
            self.root.after(1000, self.decrement_timer)
        else:
            self.game_over()

    def game_over(self):
        self.root.withdraw()
        messagebox.showinfo("Game Over", f"Your final score is {self.score} out of {len(self.questions)}")
        self.root.destroy()

if __name__ == "__main__":
    quiz = Quiz()
    quiz.start_quiz()
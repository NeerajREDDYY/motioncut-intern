import tkinter as tk
from tkinter import messagebox

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Creative Quiz Game")
        self.root.geometry("600x400")
        self.question_number = 0
        self.score = 0
        self.questions = [
            {
                "question": "What is the capital of France?",
                "options": ["London", "Berlin", "Madrid", "Paris"],
                "answer": "Paris"
            },
            {
                "question": "Which planet is known as the 'Red Planet'?",
                "options": ["Venus", "Mars", "Jupiter", "Saturn"],
                "answer": "Mars"
            },
            {
                "question": "Who wrote 'Romeo and Juliet'?",
                "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Oscar Wilde"],
                "answer": "William Shakespeare"
            },
            {
                "question": "What is the chemical symbol for gold?",
                "options": ["Au", "Ag", "Fe", "Cu"],
                "answer": "Au"
            },
            {
                "question": "In what year did the Titanic sink?",
                "options": ["1905", "1912", "1920", "1931"],
                "answer": "1912"
            }
        ]
        self.create_widgets()
        self.display_question()

    def display_question(self):
        if self.question_number < len(self.questions):
            question = self.questions[self.question_number]
            self.question_label.config(text=question["question"])
            self.option_selected.set(0)  # Clear previously selected option
            for i in range(len(question["options"])):
                self.radiobutton_list[i].config(text=question["options"][i])
            self.root.bind("<Return>", self.evaluate_answer)
        else:
            self.finish_quiz()

    def evaluate_answer(self, event=None):
        selected_option = self.option_selected.get()
        question = self.questions[self.question_number]
        if selected_option != 0 and question["options"][selected_option - 1] == question["answer"]:
            self.score += 1
        self.question_number += 1
        self.display_question()

    def finish_quiz(self):
        score_percentage = (self.score / len(self.questions)) * 100
        messagebox.showinfo("Quiz Complete", f"You scored {self.score}/{len(self.questions)} ({score_percentage:.2f}%)")
        self.root.destroy()

    def create_widgets(self):
        self.question_label = tk.Label(self.root, text="", wraplength=500, justify="center", font=("Helvetica", 16))
        self.question_label.pack(pady=20)

        self.option_selected = tk.IntVar()
        self.option_selected.set(0)  # Initialize to 0
        self.radiobutton_list = []
        for i in range(4):
            radiobutton = tk.Radiobutton(self.root, text="", variable=self.option_selected, value=i + 1, font=("Helvetica", 12))
            radiobutton.pack(pady=5)
            self.radiobutton_list.append(radiobutton)

        next_button = tk.Button(self.root, text="Next", command=self.evaluate_answer)
        next_button.pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    quiz_game = QuizGame(root)
    root.mainloop()
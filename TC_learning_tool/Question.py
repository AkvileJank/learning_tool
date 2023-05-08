import random
from copy import deepcopy

class Question:
    def __init__(
        self,
        type,
        q_text,
        answer,
        id=None,
        status="Enabled",
        showed_times=0,
        answered_correct=0,
        answered_percentage=0,
    ):
        self.q_text = q_text.capitalize()
        self.answer = answer
        self.type = type
        self.status = status
        self.id = id
        self.showed_times = showed_times
        self.answered_correct = answered_correct
        self.answered_percentage = answered_percentage

    def __str__(self):
        if self.type == "f":
            return f"{self.q_text}"
        elif self.type == "q":
            to_print_answer = deepcopy(self.answer)
            random.shuffle(to_print_answer)
            return f"{self.q_text}\n{to_print_answer[0]}\n{to_print_answer[1]}\n{to_print_answer[2]}"

    def calculate_answered_percentage(self):
        try:
            self.answered_percentage = round(
                float(self.answered_correct / self.showed_times) * 100
            )
        except ZeroDivisionError:
            pass  # equal to 0 by default

    def details(self):
        if self.type == "q":
            details = {
                "ID": self.id,
                "Type": self.type,
                "Status": self.status,
                "Q": self.q_text,
                "Correct_A": self.answer[0],
                "Incorrect_A1": self.answer[1],
                "Incorrect_A2": self.answer[2],
                "Showed_times": self.showed_times,
                "Answered_correct": self.answered_correct,
                "Answered_correct(%)": self.answered_percentage,
            }
        elif self.type == "f":
            details = {
                "ID": self.id,
                "Type": self.type,
                "Status": self.status,
                "Q": self.q_text,
                "Correct_A": self.answer,
                "Showed_times": self.showed_times,
                "Answered_correct": self.answered_correct,
                "Answered_correct(%)": self.answered_percentage,
            }
        return details

    def show_statistics(self):
        return (
            f"Question: {self.q_text}"
            "\n"
            f"ID: {self.id}, Type: {self.type}, Status: {self.status}, \
Times showed: {self.showed_times}, Answered correctly(%): {self.answered_percentage}%"
        )

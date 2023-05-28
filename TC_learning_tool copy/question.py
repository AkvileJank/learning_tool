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
            return f"{self.q_text}\n{to_print_answer[0].capitalize()}\n{to_print_answer[1].capitalize()}\n{to_print_answer[2].capitalize()}"

    def calculate_answered_percentage(self):
            self.answered_percentage = round(
                float(self.answered_correct) / float(self.showed_times) * 100
            )

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
    
    @classmethod
    def get_enabled_questions(cls, all_questions):
        enabled_questions = []
        for question in all_questions:
            if question.status == "Enabled":
                enabled_questions.append(question)
        return enabled_questions
    
    @classmethod
    def get_all_ids(cls, all_questions):
        taken_ids = []
        if not all_questions:
            return taken_ids
        else:
            for question in all_questions:
                taken_ids.append(question.id)
            return taken_ids

    @classmethod     
    def get_weights(cls, all_questions):
        weights_list = []
        for question in all_questions:
            weights_list.append(100 - question.answered_percentage)
        return tuple(weights_list)

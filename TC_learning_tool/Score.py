from datetime import datetime

class Score:
    def __init__(self, correct=0, total=0, date_time=datetime.now()):
        self.correct = correct
        self.total = total
        self.date_time = date_time

    def __str__(self):
        return f"Score: {self.correct}/{self.total}, date: {self.date_time}"
    
    def show_to_user(self):
        return f"Your score is: {self.correct}/{self.total}"

    def update_test_results(self):
        result_file = open("results.txt", "a")
        result_file.write(f"{self.__str__()}\n")

from datetime import datetime

class Score:
    def __init__(self, correct=0, total=0, percentage=0):
        self.correct = correct
        self.total = total
        self.percentage = percentage
        self.date_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def __str__(self):
        return f"Score: {self.percentage}%, date: {self.date_time}"
    
    def calculate_percentage(self):
        self.percentage = round(float(self.correct/self.total)*100)
    
    def show_to_user(self):
        return f"Your score is: {self.percentage}%"


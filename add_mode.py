import re
from question import Question


class Add_mode:
    def add_answer(self, q_type):
        if q_type == "f":
            answer = input("Answer: ").lower()
        elif q_type == "q":
            correct_answer = input("Correct answer: ").lower()
            answer2 = input("Incorrect answer: ").lower()
            answer3 = input("Alternative incorrect answer: ").lower()
            answer = [correct_answer, answer2, answer3]
        return answer

    def create_questions(self, all_questions):
        taken_ids = Question.get_all_ids(all_questions)
        print('Available types of questions are: "q" for quiz and "f" for free-form.')
        try:
            type = input("Type of question (to stop, press ctrl + c): ")
        except KeyboardInterrupt:
            return False
        match = re.match(r"^f{1}$|^q{1}$", type)
        if not match:
            print("Invalid input. Type can be q for quiz or f for free-form")
            return
        q_text = input("Question: ").capitalize()
        if q_text.isspace() or not q_text:
            print("No question entered, try again.")
            return
        answer = self.add_answer(type)
        if answer.isspace() or not answer:
            print("No answer entered, try again")
            return
        else:
            if not all_questions:
                id = 1
            else:
                id = taken_ids[len(all_questions) - 1] + 1
                # id = taken_ids[-1] + 1

            question = Question(type, q_text, answer, id)
            all_questions.append(question)
            print("Question was added successfully!")

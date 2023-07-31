import random
from question import Question


class Practice_mode:
    def practice(self, all_questions):
        print("To exit session, press ctrl+c anytime.")
        practicing = True
        while practicing:
            questions_weights = Question.get_weights(all_questions)
            question = random.choices(all_questions, weights=questions_weights)[0]
            print(question)
            try:
                question.showed_times += 1
                user_answer = input("Your answer: ").lower()
                if question.type == "f":
                    if question.answer != user_answer:
                        print("Your answer is incorrect.")
                        print(f"Correct answer is: {question.answer}")
                    else:
                        print("Correct!")
                        question.answered_correct += 1
                elif question.type == "q":
                    if question.answer[0] != user_answer:
                        print("Your answer is incorrect.")
                        print(f"Correct answer is: {question.answer[0]}")
                    else:
                        print("Correct!")
                        question.answered_correct += 1
                question.calculate_answered_percentage()
            except KeyboardInterrupt:
                break
        print("\nYour practice is finished!")

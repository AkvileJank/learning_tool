import random

class Test_mode:

    def get_amount_for_test(self, all_questions):
        while True:
            try:
                number_of_questions = int(
                    input(
                        "How many question you'd like to answer? (to exit, press ctrl+c) "
                    )
                )
                if number_of_questions > len(all_questions):
                    raise ValueError()
                return number_of_questions
            except ValueError:
                if number_of_questions > len(all_questions):
                    print(
                        f"There are only {len(all_questions)} questions active, try again."
                    )
                else:
                    print("Input is not valid, try again.")
                continue
            except KeyboardInterrupt:
                return None
            
    def collect_test_questions(self, all_questions):
        number_of_questions = self.get_amount_for_test(all_questions)
        if not number_of_questions:
            return None
        test_questions = random.sample(all_questions, k=number_of_questions)
        return test_questions
    
    def testing(self, test_questions, score):
        if not test_questions:
            return None
        score.total = len(test_questions)
        for question in test_questions:
            print(question)
            question.showed_times += 1
            user_answer = input("Your answer: ").lower()
            if question.type == "f":
                if question.answer != user_answer:
                    print("Answer is incorrect.")
                else:
                    print("Correct!")
                    score.correct += 1
                    question.answered_correct += 1
            elif question.type == "q":
                if question.answer[0] != user_answer:
                    print("Answer is incorrect.")
                else:
                    print("Correct!")
                    score.correct += 1
                    question.answered_correct += 1
            question.calculate_answered_percentage()
    

    
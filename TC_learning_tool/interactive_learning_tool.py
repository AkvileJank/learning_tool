import random
import json
import re
from question import Question
from score import Score


def main():
    mode_rules()
    all_created_questions = get_existing_questions()
    enabled_questions = get_enabled_questions(all_created_questions)
    while True:
        mode = input("\nMode you want to access: ").lower()
        if mode == "add":
            create_questions(all_created_questions)
            update_questions_file(all_created_questions)
        elif mode == "d/e":
            change_status_by_id(all_created_questions)
        elif mode == "test":
            if len(enabled_questions) < 5:
                print(
                    "Not enough enabled questions, make sure at least 5 questions are enabled"
                )
                continue
            test_questions = collect_test_questions(enabled_questions)
            if not test_questions:
                continue
            score = Score()
            test_mode(enabled_questions, test_questions, score)
        elif mode == "practice":
            if len(enabled_questions) < 5:
                print(
                    "Not enough enabled questions, make sure at least 5 questions are enabled"
                )
                continue
            practice_mode(enabled_questions)
        elif mode == "stats":
            print_statistics(all_created_questions)
        elif mode == "exit":
            print("Thanks for using!")
            break
        else:
            print("Entered mode is not found, try again")


def mode_rules():
    print(
        '\nChoose mode by entering:\n"add" for adding questions mode\n\
"d/e" for disable/enable mode\n"stats" for statistics mode\n"practice"\
 for practice mode\n"test" for test mode\nTo exit program, type "exit" '
    )


# List of objects created from json file data
def get_existing_questions():
    questions_as_obj = []
    file = open("questions_bank.json")
    try:
        file_data = json.load(file)
    except:
        return []
    for line in file_data:
        id = line["ID"]
        type = line["Type"]
        status = line["Status"]
        q_text = line["Q"]
        if type == "f":
            answer = line["Correct_A"]
        else:
            answer = [line["Correct_A"], line["Incorrect_A1"], line["Incorrect_A2"]]
        showed_times = line["Showed_times"]
        answered_correct = line["Answered_correct"]
        answered_percentage = line["Answered_correct(%)"]
        question_obj = Question(
            type,
            q_text,
            answer,
            id,
            status,
            showed_times,
            answered_correct,
            answered_percentage,
        )
        questions_as_obj.append(question_obj)
    file.close()
    return questions_as_obj


# Returns a list of enabled questions for test and practice
def get_enabled_questions(all_questions):
    enabled_questions = []
    for question in all_questions:
        if question.status == "Enabled":
            enabled_questions.append(question)
    return enabled_questions


# Choose answer input and return answer
def get_answer(q_type):
    if q_type == "f":
        answer = input("Answer: ").lower()
    elif q_type == "q":
        correct_answer = input("Correct answer: ").lower()
        answer2 = input("Incorrect answer: ").lower()
        answer3 = input("Alternative incorrect answer: ").lower()
        answer = [correct_answer, answer2, answer3]
    return answer


# Create a list of ID's that are already taken
def get_all_ids(all_questions):
    taken_ids = []
    if not all_questions:
        return taken_ids
    else:
        for question in all_questions:
            taken_ids.append(question.id)
        return taken_ids


# Add new questions from user input to questions' list, returns question's list
def create_questions(all_questions):
    taken_ids = get_all_ids(all_questions)
    print('Available types of questions are: "q" for quiz and "f" for free-form.')
    while True:
        try:
            type = input("Type of question (to stop, press ctrl + c): ")
        except KeyboardInterrupt:
            break
        match = re.match(r"^f{1}$|^q{1}$", type)
        if not match:
            print("Invalid input. Type can be q for quiz or f for free-form")
            continue
        q_text = input("Question: ").capitalize()
        if q_text.isspace() or not q_text:
            print("No question entered, try again.")
            continue
        answer = get_answer(type)
        if answer.isspace() or not answer:
            print("No answer entered, try again")
            continue
        id = random.randint(111, 999)
        find_id = True
        while find_id:
            if id in taken_ids:
                id = random.randint(111, 999)
            else:
                find_id = False

        question = Question(type, q_text, answer, id)
        all_questions.append(question)
        print("Question was added successfully!")


# Add questions to json file or update current questions
def update_questions_file(all_questions):
    all_questions_details = []
    for object in all_questions:
        all_questions_details.append(object.details())
    file_json = open("questions_bank.json", "w")
    json.dump(all_questions_details, file_json)
    file_json.close()


# Find question object by provided ID and change the status, by default is "Enabled"
def change_status_by_id(all_questions):
    while True:
        try:
            id_input = int(
                input(
                    "Enter ID of the question you want to modify, to stop press ctrl+c: "
                )
            )
        except KeyboardInterrupt:
            break
        except ValueError:
            print("Input is not valid, please try again")
            continue
        for question in all_questions:
            if question.id == id_input:
                if question.type == "f":
                    print(
                        f"Is this the question you want to enable/disable: (Enter y if yes, anything if not)?\
\nQuestion: {question.q_text}\nAnswer: {question.answer}\
\nCurrent status: {question.status}"
                    )
                else:
                    print(
                        f"Is this the question you want to enable/disable:(Enter y if yes, anything if not)\n{question}"
                    )
                confirmation = input()
                if confirmation == "y":
                    if question.status == "Enabled":
                        question.status = "Disabled"
                    else:
                        question.status = "Enabled"

                    print("Status is changed.")
                    update_questions_file(all_questions)


# User enters how many questions they want to answer on test mode
def get_amount_for_test(all_questions):
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


# Create a list of question objects for test mode based on what question amount user input
def collect_test_questions(all_questions):
    number_of_questions = get_amount_for_test(all_questions)
    if not number_of_questions:
        return None
    test_questions = random.sample(all_questions, k=number_of_questions)
    return test_questions


def answering_rules():
    print(
        "Important: for quiz questions please write answer from available choices,\
for free-form question write only one word!"
    )


# Updating score after test session and question's attributes after each question
# At the end of test updating results.txt and questions_bank.json files
def test_mode(all_questions, test_questions, score):
    if not test_questions:
        return None
    score.total = len(test_questions)
    answering_rules()
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

    score.calculate_percentage()
    print(score.show_to_user())
    update_questions_file(all_questions)
    score.update_test_results()


# Tuple of weights (int) for weighted random choice
def get_weights(all_questions):
    weights_list = []
    for question in all_questions:
        weights_list.append(100 - question.answered_percentage)
    return tuple(weights_list)


# Mode where questions are given randomly depending on their weight
def practice_mode(all_questions):
    answering_rules()
    print("To exit session, press ctrl+c anytime.")
    practicing = True
    while practicing:
        questions_weights = get_weights(all_questions)
        question = random.choices(all_questions, weights=questions_weights)[0]
        print(question)
        try:
            question.showed_times += 1
            user_answer = input("Your answer: ")
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
    update_questions_file(all_questions)
    print("\nYour practice is finished!")


# Information about each question is printed for a user
def print_statistics(all_questions):
    for question in all_questions:
        print(question.show_statistics())


if __name__ == "__main__":
    main()

# Link to pair-programming exercise:
# https://github.com/AkvileJank/war_game.git

import random
import json
import re
import sys
from Question import Question
from Score import Score


def main():
    mode_rules()
# List of question objects from json file to use in code later
    all_created_questions = get_existing_questions()
# List of only "enabled" question objects for practice and test modes
    enabled_questions = get_enabled_questions(all_created_questions)
# Prompt user to choose the mode they want to access:
    mode = input("Mode you want to access: ").lower()
    if mode == "add":
# Prompt user to create quiz or free-form questions
        create_questions(all_created_questions)
# Add created questions to json file
        update_questions_file(all_created_questions)
    elif mode == "d/e":
# Prompt user to enter question ID and change question status after confirmation
# function to update json file is called inside this function
        change_status_by_id(all_created_questions)
    elif mode == "test":
        if len(enabled_questions) < 5:
            sys.exit(
                "Not enough enabled questions, make sure at least 5 questions are enabled"
            )
# Create score object to store information about test score
        score = Score()
# Create a list of n not repeated question objects from "enabled" questions list
        test_questions = collect_test_questions(enabled_questions)
# User answers questions, changed questions' attributes are updated in json file
# In this function another function is called to update results.txt file with score
        test_mode(enabled_questions, test_questions, score)
    elif mode == "practice":
        if len(enabled_questions) < 5:
            sys.exit(
                "Not enough enabled questions, make sure at least 5 questions are enabled"
            )
# Score is not tracked, after each question, question object's attributes are updated,
# weights recalculated
        practice_mode(enabled_questions)
    elif mode == "stats":
        print_statistics(all_created_questions)
    else:
        print("Entered mode is not found")

def mode_rules():
    print('Choose mode by entering:\n"add" for adding questions mode\n\
"d/e" for disable/enable mode\n"stats" for statistics mode\n"practice"\
 for practice mode\n"test" for test mode ')

# When the program starts, each time a list of objects
# is created from the json file data
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
    return questions_as_obj


# Returns a list of only enabled questions from all the questions,
# enabled questions list is later used for test and practice mode
def get_enabled_questions(all_questions):
    enabled_questions = []
    for question in all_questions:
        if question.status == "Enabled":
            enabled_questions.append(question)
    return enabled_questions


# Choose answer input and return answer
# to create question object later
def get_answer(q_type):
    if q_type == "f":
        answer = input("Answer: ")
    elif q_type == "q":
        correct_answer = input("Correct answer: ")
        answer2 = input("Incorrect answer: ")
        answer3 = input("Alternative incorrect answer: ")
        answer = [correct_answer, answer2, answer3]
    return answer


# Create a list of ID's that are already taken by questions in json file
# to later check when assigning ID if it's altready taken
def get_all_ids(all_questions):
    taken_ids = []
    if not all_questions:
        return taken_ids
    else:
        for question in all_questions:
            taken_ids.append(question.id)
        return taken_ids


# Function to add new questions from user input to the already existing questions' list,
# which was created at the start of the program, returns question objects list
def create_questions(all_questions):
    taken_ids = get_all_ids(all_questions)
    print('Available types of questions are: "q" for quiz and "f" for free-form.')
    while True:
        try: 
            type = input('Type of question (to stop, press ctrl + c): ')
        except KeyboardInterrupt:
            break
        match = re.match(r"^f{1}$|^q{1}$", type)
        if not match:
            print("Invalid input. Type can be q for quiz or f for free-form")
            continue
        q_text = input("Question: ")
        if len(q_text) == 0:
            print("No question entered, try again.")
            continue
        answer = get_answer(type)
        if len(answer) == 0:
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


# Add questions to json file or update current questions after
# altering them in different modes of the program (overwrite current file)
def update_questions_file(all_questions):
    all_questions_details = []
    for object in all_questions:
        all_questions_details.append(object.details())
    file_json = open("questions_bank.json", "w")
    json.dump(all_questions_details, file_json)
    file_json.close()


# Function to find question object by provided ID and change the status of it,
# by default all questions are created with "Enabled" status
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
        for question in all_questions:
            if question.id == id_input:
                if question.type == "f":
                    print(
                        f"Is this the question you want to enable/disable: y/n?\
\nQuestion: {question.q_text}\nAnswer: {question.answer}\
\nCurrent status: {question.status}"
                    )
                else:
                    print(
                        f"Is this the question you want to enable/disable: y/n?\n{question}"
                    )
                confirmation = input()
                if confirmation == "y":
                    if question.status == "Enabled":
                        question.status = "Disabled"
                    else:
                        question.status = "Enabled"

                    print("Status is changed.")
                    update_questions_file(all_questions)


# Prompt user to enter how many questions they want to answer on test mode,
# User can't choose more questions than are available in the system
def get_amount_for_test(all_questions):
    while True:
        try:
            number_of_questions = int(input("How many question you'd like to answer? (to exit, press ctrl+c) "))
            if number_of_questions > len(all_questions):
                raise ValueError()
            break
        except ValueError:
            if number_of_questions > len(all_questions):
                print(f"There are only {len(all_questions)} questions active, try again.")
            else:
                print("Input is not valid, try again.")
            continue
        except KeyboardInterrupt:
            sys.exit()   
    return number_of_questions


# Create a list of question objects for test mode based on what question amount user input
def collect_test_questions(all_questions):
    number_of_questions = get_amount_for_test(all_questions)
    test_questions = random.sample(all_questions, k=number_of_questions)
    return test_questions

def answering_rules():
    print("Important: for quiz questions please write answer exactly as shown in choice,\
for free-form question write one word capitalized!")

# Score is updated at the beggining with how many questions are in the test
# After test session, correct_percentage attribute is updated and json file
# is overwritten based on the new attribute values
# results.txt file is also updated with score object information
def test_mode(all_questions, test_questions, score):
    score.total = len(test_questions)
    answering_rules()
    for question in test_questions:
        print(question)
        question.showed_times += 1
        user_answer = input("Your answer: ")
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
    
    print(score.show_to_user())
    update_questions_file(all_questions)
    score.update_test_results()


# Returns a tuple of weights (int) that are later used in weighted random choice
# Weight for each question object is calculated in a way that questions with
# less answered correct percentage would have higher weight
def get_weights(all_questions):
    weights_list = []
    for question in all_questions:
        weights_list.append(100 - question.answered_percentage)
    return tuple(weights_list)


# Similar to test mode, but questions are given randomly depending on their weight
# Score is not tracked this time
def practice_mode(all_questions):
    answering_rules()
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
            input(
            'To stop, press ctrl+c, to continue enter any other key. ')
        except KeyboardInterrupt:
            break
    update_questions_file(all_questions)
    print("\nYour practice is finished!")


# For statistics mode, information about each question object
# is printed out in informative way for a user
def print_statistics(all_questions):
    for question in all_questions:
        print(question.show_statistics())


if __name__ == "__main__":
    main()


# Link to pair-programming exercise:
# https://github.com/AkvileJank/war_game.git

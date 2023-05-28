from fileIO import FileIO
from session import Session
from add_mode import Add_mode
from disable_enable_mode import Disable_enable_mode
from test_mode import Test_mode
from practice_mode import Practice_mode
from question import Question
from score import Score

def main():
    working = True
    while working:
        file = FileIO()
        all_questions = file.get_existing_questions()
        enabled_questions = Question.get_enabled_questions(all_questions)
        session = Session(all_questions, enabled_questions, file)
        session.rules()
        if choose_mode(session, file) == False:
            working = False
    
def choose_mode(session, file):
    # try:
    mode = input("\nMode you want to access: ").lower()
    if mode == "add":
        add_mode = Add_mode()
        session.add_questions(add_mode)
    elif mode == "d/e":
        disable_enable_mode = Disable_enable_mode ()
        session.disable_enable(disable_enable_mode)
    elif mode == "stats":
        session.statistics()
    elif mode == "test" or mode == "practice":
        if len(session.enabled_questions) < 5:
            print(
                "Not enough enabled questions, make sure at least 5 questions are enabled"
            )
            return
        if mode == "test":
            score = Score()
            test_mode = Test_mode()
            if session.test(test_mode, score, file) == False:
                pass
        else:
            practice_mode = Practice_mode()
            session.practice(practice_mode)
    elif mode == "exit":
        return False
    else:
        print("Invalid input, please try again.")
    # except:
    #     print('Sorry, something went wrong. Please try again. To exit, type "exit"')

if __name__ == "__main__":
    main()

            

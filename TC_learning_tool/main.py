from fileIO import FileIO
from session import Session
from question import Question
from score import Score
from selecting_modes import Selecting_modes


def main():
    working = True
    while working:
        try:
            file = FileIO()
            all_questions = file.get_existing_questions()
            enabled_questions = Question.get_enabled_questions(all_questions)
            session = Session(all_questions, enabled_questions, file)
            score = Score()
            session.rules()
            selecting_modes = Selecting_modes()
            mode = selecting_modes.mode_input(enabled_questions)
            if mode == False:
                working = False
            selecting_modes.call_mode(mode, session, score, file)
        except KeyboardInterrupt:
            working = False
        except:
            print("Sorry, something went wrong. Try again.")


if __name__ == "__main__":
    main()

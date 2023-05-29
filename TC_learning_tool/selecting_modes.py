from add_mode import Add_mode
from disable_enable_mode import Disable_enable_mode
from test_mode import Test_mode
from practice_mode import Practice_mode
from statistics_mode import Statistics_mode

class Selecting_modes:
    def mode_input(self, enabled_questions):
        modes = {
            "add": Add_mode(),
            "d/e": Disable_enable_mode(),
            "stats": Statistics_mode(),
            "test": Test_mode(),
            "practice": Practice_mode()
        }
        mode = input("\nMode you want to access: ").lower()
        if mode in modes:
            if mode == "test" or mode == "practice":
                if self.check_question_amount(enabled_questions) == False:
                    print("Not enough enabled questions")
                    return False
            return modes[mode]
        elif mode == "exit":
            return False
        else:
            print("Input is not valid, please try again")
    
    def call_mode(self, mode, session, score, file):
        match mode:
            case Add_mode():
                session.add_questions(mode)
            case Disable_enable_mode():
                session.disable_enable(mode)
            case Statistics_mode():
                session.statistics(mode)
            case Test_mode():
                if session.test(mode, score, file) == False:
                    pass
            case Practice_mode():
                session.practicing(mode)

    def check_question_amount(self, enabled_questions):
        if len(enabled_questions) <= 5:
            return False

class Session:

    def __init__(self, all_questions, enabled_questions, json_file):
        self.all_questions = all_questions
        self.enabled_questions = enabled_questions
        self.json_file = json_file

    def rules(self):
        print(
        '\nChoose mode by entering:\n"add" for adding questions mode\n\
"d/e" for disable/enable mode\n"stats" for statistics mode\n"practice"\
 for practice mode\n"test" for test mode\nTo exit program, type "exit" '
    )

    def answering_rules(self):
        print(
            "Important: for quiz questions please write answer from available choices,\
for free-form question write only one word!"
        )

    def add_questions(self, add_mode):
        while True:
            if add_mode.create_questions(self.all_questions) == False:
                break
            self.json_file.update_questions_file(self.all_questions)
        
    
    def disable_enable(self, disable_enable_mode):
        disable_enable_mode.change_status(self.all_questions)
        self.json_file.update_questions_file(self.all_questions)

    def test(self, test_mode, score, txt_file):
        test_questions = test_mode.collect_test_questions(self.enabled_questions)
        if not test_questions:
            return False
        self.answering_rules()
        test_mode.testing(test_questions, score)
        score.calculate_percentage()
        print(score.show_to_user())
        self.json_file.update_questions_file(self.all_questions)
        txt_file.update_test_results(score)

    def practicing(self, practice_mode):
        self.answering_rules()
        practice_mode.practice(self.enabled_questions)
        self.json_file.update_questions_file(self.all_questions)

    def statistics(self, statistics_mode):
        statistics_mode.print_statistics(self.all_questions)






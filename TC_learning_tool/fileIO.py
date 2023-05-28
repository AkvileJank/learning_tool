import json
from question import Question

class FileIO:

    def get_existing_questions(self):
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
    
    def update_questions_file(self, all_questions):
        all_questions_details = []
        for object in all_questions:
            all_questions_details.append(object.details())
        file_json = open("questions_bank.json", "w")
        json.dump(all_questions_details, file_json)
        file_json.close()

    def update_test_results(self, score):
        result_file = open("results.txt", "a")
        result_file.write(f"{score.__str__()}\n")
        result_file.close()
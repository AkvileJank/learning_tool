
class Disable_enable_mode:

    def change_status(self, all_questions):
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
from interactive_learning_tool import get_all_ids, get_enabled_questions, get_weights
#WORKS
def test_get_all_ids():
    class Question:
        def __init__(self, id):
            self.id = id
    all_questions = [
        Question(111),
        Question(222),
        Question(333),
    ]
    result = get_all_ids(all_questions)
    expected = [111, 222, 333]
    assert result == expected


#WORKS
def test_get_weights():
    class Question:
        def __init__(self, answered_percentage):
            self.answered_percentage = answered_percentage

    all_questions = [
        Question(0),
        Question(50),
        Question(100),
    ]

    result = get_weights(all_questions)
    expected = (100, 50, 0)
    assert result == expected

def test_get_enabled_questions():
    class Question:
        def __init__(self, status):
            self.status = status

    all_questions = [
        Question("Enabled"),
        Question("Disabled"),
        Question("Enabled"),
    ]

    result = len(get_enabled_questions(all_questions))
    expected = 2
    assert result == expected



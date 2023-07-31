from question import Question


def test_get_all_ids():
    all_questions = [
        Question(type=None, q_text="", answer=None, id=1),
        Question(type=None, q_text="", answer=None, id=2),
        Question(type=None, q_text="", answer=None, id=3),
    ]
    result = Question.get_all_ids(all_questions)
    expected = [1, 2, 3]
    assert result == expected


def test_get_weights():
    all_questions = [
        Question(type=None, q_text="", answer=None, answered_percentage=0),
        Question(type=None, q_text="", answer=None, answered_percentage=50),
        Question(type=None, q_text="", answer=None, answered_percentage=100),
    ]
    result = Question.get_weights(all_questions)
    expected = (100, 50, 0)
    assert result == expected


def test_get_enabled_questions():
    all_questions = [
        Question(type=None, q_text="", answer=None, status="Enabled"),
        Question(type=None, q_text="", answer=None, status="Disabled"),
        Question(type=None, q_text="", answer=None, status="Enabled"),
    ]
    result = len(Question.get_enabled_questions(all_questions))
    expected = 2
    assert result == expected

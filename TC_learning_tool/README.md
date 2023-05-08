# TC_learning_tool

Welcome to ineractive learning tool!

This tool has 5 modes which are accessed with different keywords to type:
    1. Adding questions mode - "add"
    2. Statistics mode - "stats"
    3. Disable/enable questions mode - "d/e"
    4. Practice mode - "practice"
    5. Test mode - "test"

Adding questions mode:
    User will be asked to input what type of question they'd like to add. 
    User can choose from "f" for free-form and "q" for quiz question.

    For quiz questions: user needs to input question and 3 answer options, first one is correct,
    other 2 are alternative incorrect options to display later in test or practice.

    For free-form questions: user needs to input question and one capitalized word answer.

Statistics mode:
    Data about each question in the system is printed out for the user.

Disable/enable questions mode:
    By default, all added questions at first are enabled. User can change that in this mode,
    by typing question's ID number and confirming the change.

Practice mode:
    All enabled questions are chosen for user to answer. 
    Correct answers are revealed if user answers incorrectly.
    Questions that were answered correct less in test and practice mode are likely to appear more times.

Test mode:
    User chooses how many questions they want to answer.
    Score is shown at the end of the test and updated in .txt file to keep score history.
    Correct ansswers are not shown if user answers incorrectly.





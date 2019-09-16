"""
Responsible for managing quiz
"""

import random
from file_reader import FileReader


class QuizSystem:
    """
    Handle and manage quiz
    """
    questions = None
    keys = None

    def __init__(self):
        """
        Initialize questions and keys from file
        """
        reader = FileReader()
        self.questions = reader.get_questions()

    def start_quiz(self):
        """
        start quiz
        """
        # shuffle questions
        random.shuffle(self.questions)
        self.show_questions()
        quiz_result = self.get_answers()
        self.show_result(quiz_result)

    def show_questions(self):
        """
        Print list of questions
        """
        print("--------------------Questions-------------------")
        for index, question in enumerate(self.questions):
            print(index + 1, ". ", question.question_text)

    def get_answers(self):
        """
        Read input from user and compile result
        """
        quiz_result = list()
        print("------------------Give Answers------------------")

        for question_no, question in enumerate(self.questions):
            user_answer = input("Question - " + str(question_no + 1) + " :")
            result = self.evaluate_result(question, user_answer, question_no)
            quiz_result.append(result)

        return quiz_result

    @staticmethod
    def evaluate_result(question, user_answer, question_no):
        """
        Evaluate user answer
        """
        result = question.is_correct(user_answer)
        if result:
            return "Your answer for Question-{} is correct".format(question_no + 1)
        else:
            return "Sorry, the correct answer of Question-{} is {}"\
                    .format(str(question_no + 1), question.answer)

    @staticmethod
    def show_result(quiz_result):
        """
        Print list of questions
        """
        print("---------------------Result---------------------")
        for result_text in quiz_result:
            print(result_text)

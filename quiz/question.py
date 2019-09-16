"""
Represents question module
"""


class Question:
    """
    Hold quiz questions
    """
    def __init__(self,
                 question_id,
                 question_text,
                 answer):
        """
        Initialize question object
        """
        self.question_id = question_id
        self.question_text = question_text
        self.answer = answer

    def is_correct(self,
                   user_answer):
        """
        Check if answer is correct
        """
        return user_answer.lower() == self.answer.lower()

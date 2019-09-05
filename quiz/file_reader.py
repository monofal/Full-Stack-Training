"""
Module handle file operations
"""
import re

from question import Question


class FileReader:
    """
    Class to perform file operations
    """
    file_format = None

    def __init__(self):
        self.file_format = '^\d+[\.]\s.*';

    @staticmethod
    def read_file(file_path):
        """
        Read keys from file and return list of keys
        """
        file_content = None
        try:
            with open(file_path) as f:
                file_content = f.read().splitlines()
        except FileNotFoundError:
            raise

        return file_content

    def get_questions(self):
        """
        Read questions from file and return list of questions
        """
        questions = []
        try:
            question_content = self.read_file("questions.txt")
            key_content = self.read_file("key.txt")

            for question, key in zip(question_content, key_content):
                if self.validate_format(question) and self.validate_format(key):
                    # Read first character as id and from fourth character onward as text
                    questions.append(Question(question[:1], question[3:], key[3:]))
        except FileNotFoundError:
            print("File not found")

        return questions

    def validate_format(self,
                        text):
        """
        Validate if text matches the pattern
        """
        return re.match(self.file_format, text)

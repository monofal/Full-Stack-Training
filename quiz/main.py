"""
Quiz Main Module
"""

from quiz.quiz_system import QuizSystem


def main():
    """
    Main function
    """
    quiz_system = QuizSystem()
    quiz_system.start_quiz()


if __name__ == "__main__":
    main()

import random
from question import Question
from key import Key

TOTAL_QUESTIONS = 3


def read_from_file(file_name, item):
    lst_obj = []
    try:
        with open(file_name) as f:
            lines = f.read().splitlines()

            index = 1
            for l in lines:
                l = l[3:]
                if l:
                    obj = Question(index, l) if item == "question" else Key(index, l)
                    lst_obj.append(obj)
                index += 1
    except FileNotFoundError:
        print("Error: File not found.")

    return lst_obj


def print_questions(lst_questions):
    print("--------------------Questions-------------------")
    index = 1
    for q in lst_questions:
        print(index, ". ", q.question_text)
        index += 1


def start_quizz(lst_questions, lst_keys):
    lst_result = list()
    print("------------------Give Answers------------------")
    index = 0;
    while index < TOTAL_QUESTIONS:
        answer = input("Question - " + str(index + 1) + " :")
        correct_answer = next((k for k in lst_keys if lst_questions[index].question_id == k.key_id), None)
        if correct_answer is not None and correct_answer.key_text.upper() == answer.upper():
            lst_result.append("Your answer for Question-" + str(index + 1) + " is correct")
        else:
            lst_result.append(
                "Sorry, the correct answer of Question-" + str(index + 1) + " is " + correct_answer.key_text)
        index += 1
    print_result(lst_result)


def print_result(lst_result):
    print("---------------------Result---------------------")
    for r in lst_result:
        print(r)


def main():
    lst_questions = read_from_file("questions.txt", "question")
    lst_keys = read_from_file("key.txt", "key")
    random.shuffle(lst_questions)
    print_questions(lst_questions)

    start_quizz(lst_questions, lst_keys)


if __name__ == "__main__":
    main()

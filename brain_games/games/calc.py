import random

INTRO = 'What is the result of the expression?'


def get_question_and_correct_answer():
    operators = ['+', '-', '*']
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation = random.choice(operators)
    question = f'{num1} {operation} {num2}'
    correct_answer = str(eval(question))
    return correct_answer, question

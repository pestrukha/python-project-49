import random
import operator

INTRO = 'What is the result of the expression?'


def get_question_and_correct_answer():
    operators = [('+', operator.add), ('-', operator.sub), ('*', operator.mul)]
    num1 = random.randint(1, 20)
    num2 = random.randint(1, 20)
    operation, function = random.choice(operators)
    question = f'{num1} {operation} {num2}'
    correct_answer = str(function(num1, num2))
    return correct_answer, question

import random

INTRO = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def get_question_and_correct_answer():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'
    correct_answer = str(gcd(num1, num2))
    return correct_answer, question

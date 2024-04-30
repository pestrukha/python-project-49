import random

INTRO = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_game():
    question = random.randint(1, 100)
    correct_answer = 'yes' if question % 2 == 0 else 'no'
    return correct_answer, question

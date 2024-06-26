import random

INTRO = 'What number is missing in the progression?'


def get_question_and_correct_answer():
    start = random.randint(1, 50)
    step = random.randint(1, 10)
    length = 10
    progression = range(start, start + step * length, step)
    hidden_index = random.randint(0, length - 1)
    question = list(progression)
    question[hidden_index] = '..'
    question = ' '.join(str(num) if num != '..' else num for num in question)
    correct_answer = str(progression[hidden_index])
    return correct_answer, question

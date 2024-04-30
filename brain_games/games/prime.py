import random

INTRO = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_correct_answer():
    def is_prime(num):
        if num <= 1:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) is True else 'no'
    return correct_answer, question

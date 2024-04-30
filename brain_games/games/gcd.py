import random

INTRO = 'Find the greatest common divisor of given numbers.'


def generate_game():
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    question = f'{num1} {num2}'

    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    correct_answer = str(gcd(num1, num2))
    return correct_answer, question

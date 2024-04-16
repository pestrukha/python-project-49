import prompt
import random

def play_game(game_type, intro):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{intro}')
    for round_of_game in range(3):
        if game_type == 'calc':
            operations = ['+', '-', '*']
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            operation = random.choice(operations)
            question = f'{num1} {operation} {num2}'
            correct_answer = str(eval(question))

        if game_type == 'even':
            question = random.randint(1, 100)
            correct_answer = 'yes' if question % 2 == 0 else 'no'

        if game_type == 'gcd':
            num1 = random.randint(1, 100)
            num2 = random.randint(1, 100)
            question = f'{num1} {num2}'
            def gcd(a, b):
                while b:
                    a, b = b, a % b
                return a
            correct_answer = str(gcd(num1, num2))

        if game_type == 'progression':
            start = random.randint(1, 50)
            step = random.randint(1, 10)
            length = 10
            progression = [start + step * i for i in range(length)]
            hidden_index = random.randint(0, length - 1)
            question = list(progression)
            question[hidden_index] = '..'
            question = ' '.join(str(num) if num != '..' else num for num in question)
            correct_answer = str(progression[hidden_index])

        if game_type == 'prime':
            def is_prime(num):
                if num <= 1:
                    return False
                for i in range(2, num):
                    if num % i == 0:
                        return False
                return True
            question = random.randint(1, 100)
            correct_answer = 'yes' if is_prime(question) is True else 'no'

        answer = prompt.string(f'Question: {question}\n'
                               f'Your answer: ')
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
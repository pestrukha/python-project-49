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
            question = f"{num1} {operation} {num2}"
            correct_answer = str(eval(question))
        if game_type == 'even':
            question = random.randint(1, 100)
            correct_answer = 'yes' if question % 2 == 0 else 'no'

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
import prompt
import random

def play_even_game():
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'Answer "yes" if the number is even, otherwise answer "no".')
    for round_of_game in range(3):
        number = random.randint(1, 100)
        answer = prompt.string(f'Question: {number}\n'
                               f'Your answer: ')
        correct_answer = 'yes' if number % 2 == 0 else 'no'
        if answer == correct_answer:
            print('Correct!')
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')

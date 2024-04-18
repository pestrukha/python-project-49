import prompt

def play_game(game):
    name = prompt.string('Welcome to the Brain Games!\n'
                         'May I have your name? ')
    print(f'Hello, {name}!\n'
          f'{game.INTRO}')
    for round_of_game in range(3):
        correct_answer, question = game.generate_game()
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
import prompt

NUMBER_OF_ROUNDS = 3


def play_game(game):
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print(f'{game.INTRO}')
    for _ in range(NUMBER_OF_ROUNDS):
        correct_answer, question = game.get_question_and_correct_answer()
        answer = prompt.string(f'Question: {question}\n'
                               f'Your answer: ')
        if answer != correct_answer:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.\n"
                  f"Let's try again, {name}!")
            return
        print('Correct!')
    print(f'Congratulations, {name}!')

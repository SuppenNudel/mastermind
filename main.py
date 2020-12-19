import random


def guess():
    user_input = input("Enter your guess: ")
    if user_input == 'quit':
        return user_input
    input_split = tuple(map(int, tuple(user_input)))
    return input_split


def compare(the_guess, correct):
    correct_location = 0
    wrong_location = 0
    for key, pos in enumerate(the_guess):
        if correct[key] == pos:
            correct_location += 1
        elif pos in correct:
            wrong_location += 1
    return correct_location, wrong_location


def start_game():
    correct = tuple(random.randint(1, 6) for pos in range(4))
    while True:
        the_guess = guess()
        if the_guess == 'quit':
            print(f'The correct configuration was {correct}')
            break
        if the_guess == correct:
            print(f'{correct} was correct')
            break
        else:
            comparison = compare(the_guess, correct)
            print(f'{comparison[0]} are correct, {comparison[1]} have the wrong location')


# 4-stelliger Code
# aus 6 verschiedenen Farben
# eine Farbe kann mehrfach verwendet werden

# beim Raten, wie viele in Farbe und Position richtig -> schwarz
# und wie viele zwar die Farbe richtig, aber die Position falsch sind -> weiß


if __name__ == '__main__':
    start_game()

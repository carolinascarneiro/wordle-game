import random
import time
import numpy as np
from typing import Counter

wordles = ['swift', 'start', 'drift']

def welcome_and_explanation():
    print('Welcome to Wordle!')
    time.sleep(1)
    print('Wordle is a game where players have to guess a mystery five-letter word, known as the “wordle” in six attempts.')

def pick_random_wordle():
    random_index = random.randrange(0, len(wordles))
    random_wordle = wordles[random_index]
    return random_wordle

def take_guess():
    guess = input('Please input your guess here: ')
    return guess

def game():
    random_wordle = pick_random_wordle()
    print(random_wordle)
    counter = 0
    guess = take_guess()
    i_indexes = []
    if guess != random_wordle:
        random_wordle_covered = ["X", "X", "X", "X", "X"]
        for i in guess:
            if i in random_wordle:
                random_wordle_covered[guess.index(i)] = i
    print(random_wordle_covered)
        #     values = np.array([random_wordle])
        #     print(values)
        #     searchval = i
        #     ii = np.where(values == searchval)[0]
        # print(ii)

                
    # print(random_wordle_covered)

                    

#         counter += 1
#         guess = input('Your guess is wrong, please try again: ')
#         if counter == 7:
#             print('Your time is out')
#     print('You won!')
#     repeat_game()

# def repeat_game():
#     repeat_answer = input('Do you wanna play again?')
#     if repeat_answer.lower() == 'yes':
#         game()
#     else:
#         print("Wordle is closing now... thank you for participating!")
        
game()
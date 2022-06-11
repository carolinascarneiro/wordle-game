import random
import time
from turtle import position
import pandas as pd
from typing import Counter

# importing csv file
column_names = ["Inds", "Words"]
df = pd.read_csv("5_letter_words.csv", names=column_names)
wordles = df.Words.to_list()

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

def compare_strings(guess, random_wordle):
    results = {}
    for position, character in enumerate(guess):
        key = character + str(position)
        if guess[position] == random_wordle[position]:
            results[key] = f"{guess[position]}: 🟩"
        elif character in random_wordle:
            results[key] = f"{guess[position]}: 🟨"
        else:
            results[key] = f"{guess[position]}: ⬜"
    return list(results.values())

def game():
    welcome_and_explanation()
    random_wordle = pick_random_wordle()
    print(random_wordle)
    counter = 0
    guess = take_guess()
    while guess != random_wordle:
        counter += 1
        print(compare_strings(guess, random_wordle))
     
        guess = input('Your guess is wrong, please try again: ')
        if counter == 7:
            print('Your time is out')
    print(compare_strings(guess, random_wordle))
    print('You won!')
    repeat_game()

def repeat_game():
    repeat_answer = input('Do you wanna play again? ')
    if repeat_answer.lower() == 'yes':
        game()
    else:
        print("Wordle is closing now... thank you for participating!")
        
game()



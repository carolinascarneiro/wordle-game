guess = "start"
random_wordle="swiat"
results = {}

def compare_strings(guess, random_wordle):
    for position, character in enumerate(guess):
            key = character + str(position)
            if guess[position] == random_wordle[position]:
                results[key] = "🟩"
            elif character in random_wordle:
                results[key] = "🟨"
            else:
                results[key] = "⬜"
    return results.values()

print(results)
# def pretty_print():

word = random.choice(word_list)
print(word)
small_word = word.lower()
choice = list(small_word)

def check_guess(guess):
    if guess == choice and guess.islower():
        print(f'Good guess! {guess} is in the word')
        ask_for_input()

def ask_for_input():
    guess = input('Please enter a sigular letter: ')
    check_guess(guess)
    while len(choice):
        if guess.islower():
            print(f'Valid guess!')
        else:
            print(f'Invalid guess! Try lowercase letter')
            check_guess(guess)

ask_for_input()

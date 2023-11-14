import random 

word_list = ['Apple','Banana','Guava','Mango','Orange','Watermelon', 'Strawberry', '']

class Hangman:

    #initialising the variables that will be used throughout the program 
    def __init__(self, word_list, num_lives=5):
        self.word_list = word_list
        self.num_lives = num_lives

        #defining the variable word with the random choice from the word list
        self.word = random.choice(word_list) 
        #defining the variable guessed to be replaced with empty space and ensuring that
        #the guessed is the length of the word from the list
        self.word_guessed = ['_'] * len(self.word)
        self.num_letters = len(self.word)
        self.guessed_letters = []
    
    #method to check the validity of the user input letter
    def check_guess(self, guess):
        guess = guess.lower()
        if guess in self.word:
            print(f'Good guess! {guess} is in the word')
            for idx, letter in enumerate(self.word):
                if letter == guess:
                    self.word_guessed[idx] = guess

            self.num_letters -= 1
        else:
            print(f'Sorry, {guess} is not in the word')
            self.num_lives -= 1
            print(f'You have {self.num_lives} lives left.')
        
    
    def ask_for_input(self):
        while True:
            guess = input('Please enter a letter: ')
            if guess.isaplha() != True:
                print(f'Please enter an alphabetical letter: ')
            elif len(guess) != 1:
                print(f'Please enter only one letter: ')
            elif guess in self.guessed_letters:
                print('You have already tried that letter!')
            else:
                self.check_guess(guess)
                self.guessed_letters.append(guess)

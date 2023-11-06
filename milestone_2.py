import random 

word_list = ['Apple','Banana','Guava','Mango','Orange']
print(word_list)

guess = input('Please enter a singular letter: ')

word = random.choice(word_list)
print(word)

if len(guess) == 1 and guess.isalpha():
    print('Good Guess')
else:
    print('Oops! That is not a valid input')

#Using library to randomise the word choice in the list. 
import random 

#Creatign a list of words
word_list = ['Apple','Banana','Guava','Mango','Orange']
print(word_list)

#Choosing a random word from the list
word = random.choice(word_list)
print(word)

#User engagement to play the game
guess = input('Please enter a singular letter: ')

#Checking if the word meets the condition that the user has input. 
if len(guess) == 1 and guess.isalpha():
    print('Good Guess')
else:
    print('Oops! That is not a valid input')

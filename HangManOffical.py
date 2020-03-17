'''
Created on Feb 24, 2017

@author: Krystal
'''
#Starter code for hangman assignment
#Somewhere in the game, welcome the player and give instructions
import random
from random import randint

# create a list of 10 or more words.

listy = ["apple","banana","orange","tear","happy","sad","confused","upset","king","cat"]
Randy = randint(0,9)
secretWordy = listy[Randy]

def hangman(secretWord):
    lettersGuessed = []
    availableLetters = list("abcdefghijklmnopqrstuvwxyz")
    mistakes = 8
    while mistakes > 0:
        if wordFound(secretWord, lettersGuessed):
            print("You figured it out! Good job! :D")
            break
        print(displayWord(secretWord, lettersGuessed))
        print("Available letters:", " ".join(availableLetters))
        print("You have", mistakes, "tries left")
        guess = input("What is your next letter?: ")
        if guess.lower() in availableLetters:
            availableLetters.remove(guess)
            lettersGuessed.append(guess)
            if guess in secretWord:
                print("Good Guess!")
            else:
                mistakes -= 1
                print("You were wrong! Too bad... xP")
        else:
            print("You already guessed that one")
    if mistakes == 0:
        print("Looks like you lost! xD")
    elif mistakes != 0:
        print("You won... :O\n Awe man. :/")

def displayWord(secretWord, lettersGuessed):
    word = []
    for i in secretWord:
        if i in lettersGuessed:
            word.append(i)
        else:
            word.append("_")
    return(" ".join(word))

def wordFound(secretWord, lettersGuessed):
    for i in secretWord:
        if i not in lettersGuessed:
            return False
    return True

#print(secretWordy)
hangman(secretWordy)

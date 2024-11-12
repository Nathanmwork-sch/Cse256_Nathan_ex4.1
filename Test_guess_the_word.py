#cis 256
#Nathan M
#11/12/2024

import unittest
import pytest
import random
#words are a list from wordle word examples
wordlist = ["apple", "brave", "clamp", "drink", "enter", "flask", "grape", "haste", "index", "jumpy","knack", "leapt", "mighty", "noble", "open", "plaza", "quiet", "roast", "swoop", "tiger"]

def randomword():
    return random.choice(wordlist)
def test_randomword():
    assert randomword() in wordlist
    #throws error
    #assert randomword() =="apples"
def guesstheword():
    word = randomword()
    correctguess = set()
    icorrect = 0
    print("guess the word one letter at a time,\nIf the letter is correct i will indicate it\nIf not I will also indicate it\n")
    while icorrect == 0:
        guess = input("Guess a single letter: ").lower()
        #checks for invalid input, If there's a better way to do this please let me know!
        if len(guess) != 1 or guess =='1' or guess =='2' or guess =='3' or guess =='4' or guess =='5' or guess =='6' or guess =='7' or guess =='8' or guess =='9' or guess =='0':
            print("Not Ok only one letter")
            continue #starts loop over
        #checks if it is a repeat ing the corect list no repeats here.
        if guess in correctguess:
            print("Hey you already got that one right!:\n")
            continue#starts loop over

        if guess in word:
            test_guesstheword_c(guess,word)
            correctguess.add(guess)
            print("Correct guess! ")
            # Not starting the loop over to continue to the checkfor
        else:
            test_guesstheword_i(guess,word)
            print("Incorrect, try again: \n")
            continue
        #checkfor
        if all(letter in correctguess for letter in word):
            print(f"\n\nCograts you did it: word was: {word}")
            icorrect = 1
            break
def test_guesstheword_c(guess, word):
    assert guess in word
def test_guesstheword_i(guess, word):
    assert guess not in word
if __name__ == "__main__":
    test_randomword()
    guesstheword()
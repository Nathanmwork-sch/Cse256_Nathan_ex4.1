#cis 256
#Nathan M
#11/12/2024

import random
#words are a list from wordle word examples
wordlist = ["apple", "brave", "clamp", "drink", "enter", "flask", "grape", "haste", "index", "jumpy","knack", "leapt", "mighty", "noble", "open", "plaza", "quiet", "roast", "swoop", "tiger"]

def randomword():
    return random.choice(wordlist)

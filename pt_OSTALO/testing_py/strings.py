#-----------------------------------------------------
# Python 'Evolution of Text' Program
# More programs at: usingpython.com/programs
#-----------------------------------------------------
"""
Enter some text ... program evolve the answer by testing random chars but keeps
correct bits each tim it finds it ... it calculates number of iterations/generations
needed to complete the fraze
"""

import string
import random
import time

possibleCharacters = string.ascii_lowercase + string.digits + string.ascii_uppercase + ' .,!?;:'

target = input("Enter your target text: ")
attemptThis = ''.join(random.choice(possibleCharacters) for i in range(len(target)))
attemptNext = ''

completed = False

generation = 0

while completed == False:
    print(attemptThis)
    attemptNext = ''
    completed = True
    for i in range(len(target)):
        if attemptThis[i] != target[i]:
            completed = False
            attemptNext += random.choice(possibleCharacters)
        else:
            attemptNext += target[i]
    generation += 1
    attemptThis = attemptNext
    time.sleep(0.1)

print("Target matched! That took " + str(generation) + " generation(s)")

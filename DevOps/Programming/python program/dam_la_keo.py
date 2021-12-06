import os
os.system("cls")

from random import randint

player = input()
print("your choice: ",player)
computer = randint(0,2)

if computer == 0:
    computer = "dam"
if computer == 1:
    computer = "la"
if computer == 2:
    computer = "keo"

print("computer's choice is: ",computer)

if player == computer:
    print("Tie!!!")
else:
    if player == "dam":
        if computer == "la":
            print("dam < la => computer win")
        if computer == "keo":
            print("dam > keo => you win")

    if player == "la":
        if computer == "dam":
            print("dam < la => you win")
        if computer == "keo":
            print("la < keo => computer win")

    if player == "keo":
        if computer == "la":
            print("keo > la => you win")
        if computer == "keo":
            print("dam > keo => computer win")




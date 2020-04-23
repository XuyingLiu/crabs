"""This is the main module of our craps game

usage: python3 craps.py number_of_gmaes
"""
import sys
from random import randint

print("craps game")
# num_of_games = int(sys.argv[1])
num_of_games = int(input("How many times do you want to play craps? "))
print(f"Playing {num_of_games} games...")


def craps():
    """run a round of the craps and return win or loss.

    returns: 1 or 0"""

    #print("Game Running")
    d1=randint(1,6)
    d2=randint(1,6)
    dpoint=d1+d2
    #print(f"Dice: {d1}+{d2}={dpoint}")

    if dpoint in (2,3,12):
        return 0
    elif dpoint in (7,11):
        return 1
    else:
        return trial(dpoint)

def trial(point):
    """run the trials to solve the more complex craps.

    return: 1 or 0"""

    while True: 
        d1=randint(1,6)
        d2=randint(1,6)
        dtot=d1+d2 
        #print(f"Dice: {d1}+{d2}={dtot}")

        if dtot==7:
            return 0
        elif dtot==point:
            return 1
        else:
            pass  

def multicraps(times):
    """run the craps game multiple times and return the number of wins.

    returns: int"""

    wins=0
    for _ in range(times):
        result=craps()
        #print(result)
        wins+=result
    return wins

win_count=multicraps(num_of_games)
win_rate=win_count/num_of_games*100


print(f"Result: {win_count} wins. {win_rate:.2f}% win rate")


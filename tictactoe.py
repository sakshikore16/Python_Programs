# W A P to play tic tac toe

import random

def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    zero = 'X' if xState[0] else ('O' if zState[0] else 0)
    one = 'X' if xState[1] else ('O' if zState[1] else 1)
    two = 'X' if xState[2] else ('O' if zState[2] else 2)
    three = 'X' if xState[3] else ('O' if zState[3] else 3)
    four = 'X' if xState[4] else ('O' if zState[4] else 4)
    five = 'X' if xState[5] else ('O' if zState[5] else 5)
    six = 'X' if xState[6] else ('O' if zState[6] else 6)
    seven = 'X' if xState[7] else ('O' if zState[7] else 7)
    eight = 'X' if xState[8] else ('O' if zState[8] else 8)

    print("-------------")
    print(f"| {zero} | {one} | {two} |")
    print("|---|---|---|")
    print(f"| {three} | {four} | {five} |")
    print("|---|---|---|")
    print(f"| {six} | {seven} | {eight} |")
    print("-------------")

def checkWin(xState, zState):
    wins = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]
    for win in wins:
        if sum(xState[win[0]], xState[win[1]], xState[win[2]]) == 3:
            print("\nX Won the match")
            return 1
        if sum(zState[win[0]], zState[win[1]], zState[win[2]]) == 3:
            print("\nO Won the match")
            return 0
    return -1

def computerMove(zState, xState):
    empty_cells = [i for i in range(9) if not (xState[i] or zState[i])]
    return random.choice(empty_cells)

if __name__ == "__main__":
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  
    print("Welcome to Tic Tac Toe\n")
    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("\nX's Chance")
            value = int(input("Please enter a value: "))
            xState[value] = 1
        else:
            print("\nO's Chance (Computer)")
            value = computerMove(zState, xState)
            zState[value] = 1
            print(f"Computer's choice: {value}\n")

        cwin = checkWin(xState, zState)
        if cwin != -1:
            print("\nMatch over")
            break

        turn = 1 - turn

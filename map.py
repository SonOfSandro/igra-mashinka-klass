import pygame
board = []
for i in range(32):
    temp_list = []
    for j in range(32):
        if j <= 4 or j >= 28:
            temp_list.append(0)
        else:
            temp_list.append(1)
    board.append(temp_list)
for i in board:
    for j in board[board.index(i)]:
        print(j, end="\t")
    print("", end="\n")
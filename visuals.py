import bot_A
import bot_B
import handler
import judge
import pygame
from pygame.rect import *
from tkinter import *

f = handler.neoask()


def draw(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == 1:
                COLOR = (255, 0, 0)
            elif board[y][x] == 2:
                COLOR = (100, 0, 0)
            elif board[y][x] == 3:
                COLOR = (0, 255, 0)
            elif board[y][x] == 4:
                COLOR = (0, 100, 0)
            else:
                COLOR = (0, 0, 0)
            rect = Rect(x * SIZE + 10, y * SIZE + 10, SIZE - 20, SIZE - 20)
            pygame.draw.rect(screen, COLOR, rect)
            pygame.display.flip()


SIZE = 50
pygame.init()
screen = pygame.display.set_mode((640, 440))
pygame.display.set_caption('Draughts')
running = True
board = judge.boardstartpos().copy()
boardflip = judge.boardflip(board).copy()
whitemove = True
for x in range(8):
    for y in range(8):
        rect = Rect(x * SIZE, y * SIZE, SIZE, SIZE)
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)
        pygame.display.flip()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if whitemove:
                move = bot_A.main(board)
                print(move)
                board = judge.boardmove(board, move)
                boardflip = judge.boardflip(board).copy()
                whitemove = False
                draw(board)
            else:
                move = 7777 - bot_B.main(boardflip)
                print(move)
                board = judge.boardmove(board, move)
                boardflip = judge.boardflip(board).copy()
                whitemove = True
                draw(board)

    draw(board)


pygame.quit()

import os
import time
from tkinter import *
from tkinter import filedialog
import pygame
from pygame.rect import *
import judge

try:
    f = open("bot_A.py", "r")
except:
    f = open("bot_A.py", "w")
f.close()
try:
    f = open("bot_B.py", "r")
except:
    f = open("bot_B.py", "w")
f.close()
import bot_A
import bot_B

playing = True
board = judge.boardstartpos().copy()
boardflip = judge.boardflip(board).copy()
whitemove = True


def browseFilesA():
    s = filedialog.askopenfilename(initialdir="/",
                                   title="Select a File",
                                   filetypes=(("Python file",
                                               "*.py*"),
                                              ("all files",
                                               "*.*")))

    f = open(s, "r")
    string = f.read()
    f.close()
    f = open("bot_A.py", "w")
    f.write(string)
    f.close()

    label_cpu1.configure(text=s[s.rfind('/') + 1:])
    label_file_explorer.configure(text="File Opened: " + s)


def browseFilesB():
    s = filedialog.askopenfilename(initialdir="/",
                                   title="Select a File",
                                   filetypes=(("Python file",
                                               "*.py*"),
                                              ("all files",
                                               "*.*")))
    f = open(s, "r")
    string = f.read()
    f.close()
    f = open("bot_B.py", "w")
    f.write(string)
    f.close()

    label_cpu2.configure(text=s[s.rfind('/') + 1:])
    label_file_explorer.configure(text="File Opened: " + s)


def play():
    global playing
    global board
    global boardflip
    global whitemove
    playing = True

    while playing:
        if whitemove:
            move = bot_A.main(board)
            print(move)
            if len(label_journal.cget("text")) < 247:
                label_journal.configure(text=label_journal.cget("text") + "\n" + str(move))
            else:
                label_journal2.configure(text=label_journal2.cget("text") + "\n" + str(move))
            board = judge.boardmove(board, move)
            boardflip = judge.boardflip(board).copy()
            whitemove = False
            draw(board)
            time.sleep(0.2)
        else:
            move = 7777 - bot_B.main(boardflip)
            print(move)
            if len(label_journal.cget("text")) < 247:
                label_journal.configure(text=label_journal.cget("text") + " " + str(move))
            else:
                label_journal2.configure(text=label_journal2.cget("text") + " " + str(move))
            board = judge.boardmove(board, move)
            boardflip = judge.boardflip(board).copy()
            whitemove = True
            draw(board)
            time.sleep(0.2)
        wc = 0
        bc = 0
        for y in range(8):
            for x in range(8):
                if board[y][x] == 1 or board[y][x] == 2:
                    wc += 1
                if board[y][x] == 3 or board[y][x] == 4:
                    bc += 1
        if wc == 0:
            label_victory.configure(text="Black wins")
            break
        if bc == 0:
            label_victory.configure(text="White wins")
            break
        if move == 0 or move == 7777:
            label_victory.configure(text="Draw")
            break
        try:
            window.update()
            window.update_idletasks()
        except:
            return


def clear():
    global gameend
    gameend = False
    global board
    board = judge.boardstartpos().copy()
    label_journal.configure(text="Journal")
    label_journal2.configure(text="")
    label_victory.configure(text="")
    global whitemove
    whitemove = True
    draw(board)


def stop():
    global playing
    playing = False


window = Tk()
window.title('File Explorer')
window.geometry("900x500")
window.config(background="black")
embed = Frame(window, width=400, height=400)
embed.grid(column=4, row=1, rowspan=10, columnspan=3)
os.environ['SDL_WINDOWID'] = str(embed.winfo_id())
os.environ['SDL_VIDEODRIVER'] = 'windib'
label_file_explorer = Label(window,
                            text="Select Files:",
                            width=50, height=4,
                            fg="white", background="black")
label_journal = Label(window,
                            text="Journal",
                            width=10, height=26,
                            fg="white", background="black", anchor="n")
label_journal2 = Label(window,
                            text="",
                            width=10, height=26,
                            fg="white", background="black", anchor="n")
label_cpu1 = Label(window,
                            text="NO NEW BOT LOADED",
                            width=22, height=4,
                            fg="white", background="black")
label_vs = Label(window,
                            text="VS",
                            width=10, height=4,
                            fg="white", background="black")
label_cpu2 = Label(window,
                            text="NO NEW BOT LOADED",
                            width=22, height=4,
                            fg="white", background="black")
label_victory = Label(window,
                            text="",
                            width=22, height=4,
                            fg="white", background="black")
button_explore_A = Button(window,
                          text="Bot A (Browse)",
                          command=browseFilesA, width=10)
button_explore_B = Button(window,
                          text="Bot B (Browse)",
                          command=browseFilesB, width=10)
button_play = Button(window,
                          text="Play",
                          command=play, width=10)
button_stop = Button(window,
                          text="Stop",
                          command=stop, width=10)
button_clear = Button(window,
                          text="Reset",
                          command=clear, width=10)
button_exit = Button(window,
                     text="Exit",
                     command=window.destroy, width=10)
label_file_explorer.grid(column=1, row=1, columnspan=3)
label_cpu1.grid(column=4, row=11)
label_vs.grid(column=5, row=11)
label_cpu2.grid(column=6, row=11)
label_victory.grid(column=1, row=4, columnspan=3)
label_journal.grid(column=7, row=1, rowspan=10)
label_journal2.grid(column=8, row=1, rowspan=10)
button_explore_A.grid(column=1, row=2)
button_explore_B.grid(column=2, row=2)
button_play.grid(column=1, row=3)
button_stop.grid(column=2, row=3)
button_clear.grid(column=3, row=3)
button_exit.grid(column=3, row=2)


def draw(board):
    for y in range(8):
        for x in range(8):
            if board[y][x] == 1:
                COLOR = (250, 235, 215)
            elif board[y][x] == 2:
                COLOR = (120, 120, 100)
            elif board[y][x] == 3:
                COLOR = (205, 80, 55)
            elif board[y][x] == 4:
                COLOR = (100, 35, 20)
            else:
                COLOR = (0, 0, 0)
            rect = Rect(x * SIZE + 10, y * SIZE + 10, SIZE - 20, SIZE - 20)
            pygame.draw.rect(screen, COLOR, rect)
            pygame.display.flip()


SIZE = 50
pygame.init()
screen = pygame.display.set_mode((400, 400))
pygame.display.set_caption('Draughts')
running = True
global gameend
gameend = False
board = judge.boardstartpos().copy()
boardflip = judge.boardflip(board).copy()
whitemove = True
window.update()
pygame.display.update()
for x in range(8):
    for y in range(8):
        rect = Rect(x * SIZE, y * SIZE, SIZE, SIZE)
        pygame.draw.rect(screen, (255, 255, 255), rect, 2)
        window.update()
        pygame.display.update()
draw(board)
pygame.display.update()
while running:
    try:
        pygame.display.update()
        window.update()
    except:
        running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if not gameend:
                if whitemove:
                    move = bot_A.main(board)
                    if len(label_journal.cget("text")) < 247:
                        label_journal.configure(text=label_journal.cget("text") + "\n" + str(move))
                    else:
                        label_journal2.configure(text=label_journal2.cget("text") + "\n" + str(move))
                    board = judge.boardmove(board, move)
                    boardflip = judge.boardflip(board).copy()
                    whitemove = False
                    draw(board)
                else:
                    move = 7777 - bot_B.main(boardflip)
                    if len(label_journal.cget("text")) < 247:
                        label_journal.configure(text=label_journal.cget("text") + " " + str(move))
                    else:
                        label_journal2.configure(text=label_journal2.cget("text") + " " + str(move))
                    board = judge.boardmove(board, move)
                    boardflip = judge.boardflip(board).copy()
                    whitemove = True
                    draw(board)
                wc = 0
                bc = 0
                for y in range(8):
                    for x in range(8):
                        if board[y][x] == 1 or board[y][x] == 2:
                            wc += 1
                        if board[y][x] == 3 or board[y][x] == 4:
                            bc += 1
                if wc == 0:
                    label_victory.configure(text="Black wins")
                    gameend = True
                if bc == 0:
                    label_victory.configure(text="White wins")
                    gameend = True
                if move == 0 or move == 7777:
                    label_victory.configure(text="Draw")
                    gameend = True


pygame.quit()

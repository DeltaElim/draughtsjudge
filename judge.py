asciiboard = 'w0w0w0w0' \
             '0w0w0w0w' \
             'w0w0w0w0' \
             '0e0e0e0e' \
             'e0e0e0e0' \
             '0b0b0b0b' \
             'b0b0b0b0' \
             '0b0b0b0b'


def boardclr():
    b = []
    for x in range(8):
        b.append([0, 0, 0, 0, 0, 0, 0, 0])
    return b


# 0 - empty
# 1 - white
# 2 - white crowned
# 3 - black
# 4 - black crowned
def boardstartpos():
    b = []
    b.append([0, 3, 0, 3, 0, 3, 0, 3])
    b.append([3, 0, 3, 0, 3, 0, 3, 0])
    b.append([0, 3, 0, 3, 0, 3, 0, 3])
    b.append([0, 0, 0, 0, 0, 0, 0, 0])
    b.append([0, 0, 0, 0, 0, 0, 0, 0])
    b.append([1, 0, 1, 0, 1, 0, 1, 0])
    b.append([0, 1, 0, 1, 0, 1, 0, 1])
    b.append([1, 0, 1, 0, 1, 0, 1, 0])
    return b


# starting position hash: 33954926791333464047932969545
def boardhash(b):
    bhash = 0
    num = 0
    for y in range(8):
        for x in range(8):
            if (num % 2 == 1 and (num // 8) % 2 == 0) or (num % 2 == 0 and (num // 8) % 2 == 1):
                bhash = (bhash << 3) | b[y][x]
            num += 1
    return bhash


def boardfromhash(bhash):
    b = []
    for x in range(8):
        b.append([0, 0, 0, 0, 0, 0, 0, 0])
    num = 0
    for y in range(8):
        for x in range(8):
            if (num % 2 == 1 and (num // 8) % 2 == 0) or (num % 2 == 0 and (num // 8) % 2 == 1):
                b[y][x] = (bhash & (7 << 93)) >> 93
                bhash = bhash & ((1 << 93) - 1)
                bhash = bhash << 3
            num += 1
    return b


def boardcheck(b):
    check = False
    for y in range(8):
        for x in range(8):
            if b[y][x] == 1:
                if x <= 5 and y >= 2:
                    if b[y - 1][x + 1] == 3 and b[y - 2][x + 2] == 0:
                        check = True
                if x >= 2 and y >= 2:
                    if b[y - 1][x - 1] == 3 and b[y - 2][x - 2] == 0:
                        check = True
    return check


def boardmove(b, move):
    ystart = move // 1000
    xstart = (move // 100) % 10
    yend = (move // 10) % 10
    xend = move % 10
    allowmove = False
    if 0 <= ystart <= 7 and 0 <= xstart <= 7 and 0 <= yend <= 7 and 0 <= xend <= 7:
        if b[ystart][xstart] == 1:
            if ystart - yend == 1 and abs(xstart - xend) == 1 and boardcheck(b) == False:
                if b[yend][xend] == 0:
                    allowmove = True
            if abs(ystart - yend) == 2 and abs(xstart - xend) == 2:
                if b[yend][xend] == 0 and b[(ystart + yend) // 2][(xstart + xend) // 2] == 3 or b[(ystart + yend) // 2][(xstart + xend) // 2] == 4:
                    allowmove = True

        elif b[ystart][xstart] == 2:
            if abs(ystart - yend) == abs(xstart - xend):
                clr = True
                if ystart > yend and xstart > xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart - k][xstart - k] != 0:
                            if b[ystart - k][xstart - k] == 3 or b[ystart - k][xstart - k] == 4:
                                if ystart - k - 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True

                elif ystart > yend and xstart < xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart - k][xstart + k] != 0:
                            if b[ystart - k][xstart + k] == 3 or b[ystart - k][xstart + k] == 4:
                                if ystart - k - 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True
                elif ystart < yend and xstart > xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart + k][xstart - k] != 0:
                            if b[ystart + k][xstart - k] == 3 or b[ystart + k][xstart - k] == 4:
                                if ystart + k + 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True
                elif ystart < yend and xstart < xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart + k][xstart + k] != 0:
                            if b[ystart + k][xstart + k] == 3 or b[ystart + k][xstart + k] == 4:
                                if ystart + k + 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True

        elif b[ystart][xstart] == 3:
            if ystart - yend == -1 and abs(xstart - xend) == 1 and boardcheck(boardflip(b).copy()) == False:
                if b[yend][xend] == 0:
                    allowmove = True
            if abs(ystart - yend) == 2 and abs(xstart - xend) == 2:
                if b[yend][xend] == 0 and b[(ystart + yend) // 2][(xstart + xend) // 2] == 1 or b[(ystart + yend) // 2][(xstart + xend) // 2] == 2:
                    allowmove = True

        elif b[ystart][xstart] == 4:
            if abs(ystart - yend) == abs(xstart - xend):
                clr = True
                if ystart > yend and xstart > xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart - k][xstart - k] != 0:
                            if b[ystart - k][xstart - k] == 1 or b[ystart - k][xstart - k] == 2:
                                if ystart - k - 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True

                elif ystart > yend and xstart < xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart - k][xstart + k] != 0:
                            if b[ystart - k][xstart + k] == 1 or b[ystart - k][xstart + k] == 2:
                                if ystart - k - 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True
                elif ystart < yend and xstart > xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart + k][xstart - k] != 0:
                            if b[ystart + k][xstart - k] == 1 or b[ystart + k][xstart - k] == 2:
                                if ystart + k + 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True
                elif ystart < yend and xstart < xend:
                    for k in range(1, abs(ystart - yend) + 1):
                        if b[ystart + k][xstart + k] != 0:
                            if b[ystart + k][xstart + k] == 1 or b[ystart + k][xstart + k] == 2:
                                if ystart + k + 1 == yend:
                                    allowmove = True
                                    break
                            else:
                                clr = False
                    if clr:
                        allowmove = True
    if allowmove:
        if b[ystart][xstart] == 1:
            if abs(ystart - yend) == 2:
                b[(ystart + yend) // 2][(xstart + xend) // 2] = 0
            if yend == 0:
                b[yend][xend] = 2
            else:
                b[yend][xend] = 1
        elif b[ystart][xstart] == 2:
            b[yend][xend] = 2
            b[min(ystart, yend) + abs(ystart - yend) - 1][min(xstart, xend) + abs(xstart - xend) - 1] = 0
        elif b[ystart][xstart] == 3:
            if abs(ystart - yend) == 2:
                b[(ystart + yend) // 2][(xstart + xend) // 2] = 0
            if yend == 7:
                b[yend][xend] = 4
            else:
                b[yend][xend] = 3
        elif b[ystart][xstart] == 4:
            b[yend][xend] = 4
            b[min(ystart, yend) + abs(ystart - yend) - 1][min(xstart, xend) + abs(xstart - xend) - 1] = 0

        b[ystart][xstart] = 0
    return b


def boardflip(b):
    bb = []
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    bb.append([0, 0, 0, 0, 0, 0, 0, 0])
    for y in range(8):
        for x in range(8):
            if b[7 - y][7 - x] == 1:
                bb[y][x] = 3
            elif b[7 - y][7 - x] == 2:
                bb[y][x] = 4
            elif b[7 - y][7 - x] == 3:
                bb[y][x] = 1
            elif b[7 - y][7 - x] == 4:
                bb[y][x] = 2
    return bb




# board = boardstartpos().copy()
#
#
# def getboard():
#     return board
#
# print(board)
# bhash = (boardhash(board))
# print(bhash)
# board = boardfromhash(bhash)
# print(board)
# board = boardmove(board, 5032)
# print(board)
# bhash = (boardhash(board))
# print(bhash)
# board = boardfromhash(bhash)
# print(board)

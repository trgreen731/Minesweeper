import random


def minedata():
    BombSpaces = {}
    BombDisplay = {}
    FlagDisplay = {}
    x = 0
    y = 0
    bombs = 0
    spacesleft = 64
    # assigns which spaces will be bombs with a max of 10
    # look here for changing size and number of bombs in a game
    while y < 8:
        while x < 8:
            probability = int(((10 - bombs) / spacesleft) * 100)
            total = random.randint(0, 99)
            if total <= probability and bombs < 10:
                space = "B"
                bombs += 1
                spacesleft -= 1
            else:
                space = "0"
                spacesleft -= 1
            BombSpaces[str(x)+str(y)] = space
            BombDisplay[str(x)+str(y)] = "False"
            FlagDisplay[str(x)+str(y)] = "False"
            x += 1
        x = 0
        y += 1

    x = 0
    y = 0
    # assigns the value to all spaces and skips any space that is a bomb
    # 3 cases necessary for both variables and 9 total because of edge effects when determining proximity
    # Change the 7 value when changing game size as well
    while y < 8:
        while x < 8:
            bombsnear = 0
            if BombSpaces[str(x)+str(y)] == "0":
                if y == 0:
                    if x == 0:
                        a = x
                        b = y
                        while a <= x + 1:
                            while b <= y + 1:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y
                            a += 1
                    elif x == 7:
                        a = x - 1
                        b = y
                        while a <= x:
                            while b <= y + 1:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y
                            a += 1
                    else:
                        a = x - 1
                        b = y
                        while a <= x + 1:
                            while b <= y + 1:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y
                            a += 1
                elif y == 7:
                    if x == 0:
                        a = x
                        b = y - 1
                        while a <= x + 1:
                            while b <= y:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y - 1
                            a += 1
                    elif x == 7:
                        a = x - 1
                        b = y - 1
                        while a <= x:
                            while b <= y:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y - 1
                            a += 1
                    else:
                        a = x - 1
                        b = y - 1
                        while a <= x + 1:
                            while b <= y:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y - 1
                            a += 1
                else:
                    if x == 0:
                        a = x
                        b = y - 1
                        while a <= x + 1:
                            while b <= y + 1:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y - 1
                            a += 1
                    elif x == 7:
                        a = x - 1
                        b = y - 1
                        while a <= x:
                            while b <= y + 1:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y - 1
                            a += 1
                    else:
                        a = x - 1
                        b = y - 1
                        while a <= x + 1:
                            while b <= y + 1:
                                if BombSpaces[str(a) + str(b)] == "B":
                                    bombsnear += 1
                                b += 1
                            b = y - 1
                            a += 1
                BombSpaces[str(x)+str(y)] = str(bombsnear)
            x += 1
        x = 0
        y += 1
    return BombSpaces, BombDisplay, FlagDisplay


def mineprint(BombSpaces, BombDisplay, FlagDisplay):
    cleared = 0
    gameover = 0
    while gameover == 0:
        x = 0
        y = 0
        print("     0  1  2  3  4  5  6  7\n\n0", end="    ")
        while y < 8:
            while x < 8:
                if x == 7:
                    if y == 7:
                        if BombDisplay[str(x)+str(y)] == "True":
                            print(BombSpaces[str(x)+str(y)])
                        elif FlagDisplay[str(x)+str(y)] == "True":
                            print("*")
                        else:
                            print("X")
                    else:
                        if BombDisplay[str(x)+str(y)] == "True":
                            print(BombSpaces[str(x)+str(y)] + "\n" + str(y+1), end="    ")
                        elif FlagDisplay[str(x)+str(y)] == "True":
                            print("*" + "\n" + str(y + 1), end="    ")
                        else:
                            print("X" + "\n" + str(y + 1), end="    ")
                else:
                    if BombDisplay[str(x)+str(y)] == "True":
                        print(BombSpaces[str(x)+str(y)], end="  ")
                    elif FlagDisplay[str(x)+str(y)] == "True":
                        print("*", end="  ")
                    else:
                        print("X", end="  ")
                x += 1
            x = 0
            y += 1
        print("")
        choice = input("Choose a space: ")
        if choice[0] == "f":
            if FlagDisplay[choice[1]+choice[2]] == "True":
                FlagDisplay[choice[1] + choice[2]] = "False"
            else:
                FlagDisplay[choice[1] + choice[2]] = "True"
        else:
            if 7 >= int(choice[0]) >= 0 and 7 >= int(choice[1]) >= 0:
                if BombDisplay[choice] == "False":
                    BombDisplay[choice] = "True"
                    cleared += 1
                else:
                    print("The space has already been selected.")
            else:
                print("Invalid Entry")

        if choice[0] != "f":
            if BombSpaces[choice] == "B":
                print("GameOver")
                gameover = 1
        if cleared == 54:
            print("You Win")
            gameover = 1
    return

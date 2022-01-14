#!/usr/bin/python3


def img_splitter(img):
    img_lines = img.splitlines()
    longest = 0
    for ind, line in enumerate(img_lines):
        if line == "":
            img_lines.pop(ind)
        if len(line) > longest:
            longest = len(line)
    for line in img_lines:
        if len(line) < longest:
            line.format(n=longest, c=" ")
    return img_lines


def encrypt():
    imgList = []
    letterDICT = {'A': path + 'A.txt', 'B': path + 'B.txt', 'C': path + 'C.txt', 'D': path + 'D.txt',
                  'E': path + 'E.txt',
                  'F': path + 'F.txt', 'G': path + 'G.txt', 'H': path + 'H.txt', 'I': path + 'I.txt',
                  'J': path + 'J.txt',
                  'K': path + 'K.txt', 'L': path + 'L.txt', 'M': path + 'M.txt', 'N': path + 'N.txt',
                  'O': path + 'O.txt',
                  'P': path + 'P.txt', 'Q': path + 'Q.txt', 'R': path + 'R.txt', 'S': path + 'S.txt',
                  'T': path + 'T.txt',
                  'U': path + 'U.txt', 'V': path + 'V.txt', 'W': path + 'W.txt', 'X': path + 'X.txt',
                  'Y': path + 'Y.txt',
                  'Z': path + 'Z.txt'}

    letterScan = list(engLetters)
    for alphabet in letterScan:
        if alphabet in letterDICT:
            txtScan = letterDICT[alphabet]

            with open(txtScan, 'r') as fr:
                data = fr.read()
                imgList.append(img_splitter(data))

    numLetters = len(imgList)
    zipped = zip(*imgList)
    for line in zipped:
        match numLetters:
            case 1:
                print(line[0])
            case 2:
                print(line[0], line[1])
            case 3:
                print(line[0], line[1], line[2])
            case 4:
                print(line[0], line[1], line[2], line[3])
            case 5:
                print(line[0], line[1], line[2], line[3], line[4])
            case 6:
                print(line[0], line[1], line[2], line[3], line[4], line[5])
            case 7:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6])
            case 8:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7])
            case 9:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7], line[8])
            case 10:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7], line[8], line[9])
            case 11:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7], line[8], line[9], line[10])
            case 12:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7], line[8], line[9], line[10], line[11])
            case 13:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7], line[8], line[9], line[10], line[11], line[12])
            case 14:
                print(line[0], line[1], line[2], line[3], line[4], line[5],
                      line[6].line[7], line[8], line[9], line[10], line[11], line[12], line[13])
    print('\n')


path = 'ASCII arts/'
message = input("What is your name: ")
engLetters = message.upper()
encrypt()

vm = path + "vending_machine.txt"
with open(vm, 'r') as fr:
    print(fr.read(), end='\n')

    exchange = input("Would you like something to drink? Enter Y/N ")
    if exchange.upper() == 'Y':
        print("Sorry the machine is being hacked by the Aliens")
        print("They want to know your choice by using their language")

        decision = input("Would you like do use the decoder to purchase the drink [Y/N]")
        if decision.upper() == 'N':
            message = "bye"
            engLetters = message.upper()
            print(message)
            encrypt()

        elif decision.upper() == 'Y':
            bev_choice = input("Enter you drink types [coke], [sprite], [fanta], [water], and [lemonade]")
            bev_choice = bev_choice.upper()
            engLetters = bev_choice
            encrypt()

            bev_dict = {'COKE': path + "coke.txt",
                        'SPRITE': path + 'sprite.txt',
                        'FANTA': path + 'fanta.txt',
                        'WATER': path + 'water.txt',
                        'LEMONADE': path + 'lemonade.txt'}

            if bev_choice in bev_dict:
                bevtxt = bev_dict[bev_choice]
                print("Getting your item... please wait...")
                with open(str(bevtxt), "r") as bf:
                    # indent to keep the building object open
                    # loop across the lines in the file
                    for svr in bf:
                        # print and end without a newline
                        print(svr, end="")
                print()
                print("Here you go! Enjoy it!")
                print("Thanks for purchasing! ")

    elif exchange.upper() == 'N':
        print("Please Come back when you are thirsty")

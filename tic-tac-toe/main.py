def sum(a, b, c):
    return a + b + c

def printBoard(xState, zState):
    l0 = 'X' if xState[0] else ('O' if zState[0] else 0)
    l1 = 'X' if xState[1] else ('O' if zState[1] else 0)
    l2 = 'X' if xState[2] else ('O' if zState[2] else 0)
    l3 = 'X' if xState[3] else ('O' if zState[3] else 0)
    l4 = 'X' if xState[4] else ('O' if zState[4] else 0)
    l5 = 'X' if xState[5] else ('O' if zState[5] else 0)
    l6 = 'X' if xState[6] else ('O' if zState[6] else 0)
    l7 = 'X' if xState[7] else ('O' if zState[7] else 0)
    l8 = 'X' if xState[8] else ('O' if zState[8] else 0)

    print(f' {l0} | {l1} | {l2} ')
    print(f'-----------')
    print(f' {l3} | {l4} | {l5} ')
    print(f'-----------')
    print(f' {l6} | {l7} | {l8} ')

def checkWin(xState, zState):
    xwins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
    for win in xwins:
        if sum([xState[win[0]], xState[win[1]], xState[win[2]]]) == 3:
            print('X won the match')
            return 1
        if sum([zState[win[0]], zState[win[1]], zState[win[2]]]) == 3:
            print('O won the match')
            return 0
    return -1

def mainBloc():
    xState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    zState = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    turn = 1  # 1 for X and 0 for O
    print("Welcome to Tic Tac Toe")

    while True:
        printBoard(xState, zState)

        if turn == 1:
            print("X's turn")
            value = int(input("Enter a value: "))
            xState[value] = 1
        else:
            print("O's turn")
            value = int(input("Enter a value: "))
            zState[value] = 1

        cWin = checkWin(xState, zState)
        if cWin != -1:
            break

        turn = 1 - turn

mainBloc()

board = list(range(1, 10))

wins = [(1, 2, 3), (4, 5, 6), (7, 8, 9),
        (1, 4, 7), (2, 5, 8), (3, 6, 9),
        (1, 5, 9), (3, 5, 7)]


def qwe():
    print("-------------")
    for i in range(3):
        print("|", board[0 + i * 3], "|", board[1 + i * 3], '|', board[2 + i * 3], "|")
    print("-------------")


def take_input(fg):
    while True:
        value = input("Куда поставить - " + fg+' ?')
        if not (value in '123456789'):
            print("Ошибичный ввод.Повтарите.")
            continue

        value = int(value)
        if str(board[value - 1]) in "xo":
            print("Эта клетка занята ")
            continue
        board[value - 1] = fg
        break


def win():
    for er in wins:
        if (board[er[0] - 1]) == (board[er[1] - 1]) == (board[er[2] - 1]):
            return board[er[1] - 1]
    else:
        return False


def main():
    co = 0
    while True:
        qwe()
        if co % 2 == 0:
            take_input("x")

        else:
            take_input('o')
        if co > 3:
            winner =win()
            if winner:
                qwe()
                print(winner, "Выиграл !")
                break

        co += -1
        if co > 8:
            qwe()
            print('Ничья !!!')
            break



main()
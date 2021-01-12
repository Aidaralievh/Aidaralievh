from .krestiki_noliki import positions, board, x_list, o_list, win_positions

positions = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
board = f'''
                           | {positions[0]}  | {positions[1]}  |  {positions[2]} |
                           |--------------|
                           | {positions[3]}  | {positions[4]}  |  {positions[5]} |
                           |--------------|
                           | {positions[6]}  | {positions[7]}  |  {positions[8]} |
'''

win_positions = [[0, 1, 2], [0, 4, 8], [0, 3, 6],
                 [1, 4, 7], [2, 5, 8], [2, 4, 6],
                 [3, 4, 5], [6, 7, 8]]

def detect_winner(position):
    for i in range(len(position)):
        if position[i] == 'X':
            x_list.append(i)
        if position[i] == 'O':
            o_list.append(i)

    x_set = set(x_list)
    o_set = set(o_list)
    win_x = None
    for j in win_positions:
        print(j)
        j_set = set(j)
        win_x = j_set & x_set
        win_o = j_set & o_set
        if len(win_x) == 3:
            print("Х выиграли")
            return 'X win'
        elif len(win_o) == 3:
            print("О выиграли")
            return 'O win'
        else:
            print('Игра продолжается')
            return "Game is not end"

    print(x_set)
    print(win_x)
    print(x_list)
    print()


def human_move(human_loop, human_symbol, positions_list):
    positions_2 = positions_list.copy()
    free = []
    human = human_loop - 1
    for i in range(len(positions_list)):
        if positions_2[i] not in ('X', 'O'):
            free.append(i)
    if human in free:
        positions_2[human] = human_symbol
        print(positions_2)
        return positions_2
    else:
        print('Поле уже занято!')
        return False


def computer_move(board, computer, human):
    """Делает ход копмьютер """
    # создание рабочей копии доски, потому что функция будет менятьнекоторые значения вс писке
    board = board[:]
    # поля от лучшего к худшему
    BEST_MOVES = [4, 0, 2, 6, 8, 1, 3, 5, 7]
    print("Я выберу номер", end=" ")
    for move in legal_moves(board):
        board[move] = computer
        # Если следующим хододом может победитькомпьютер,выберем тогда ход
        if winner(board) == computer:
            print(move)
            return move
        # выполним проверку, отменим внесения изменения
        board[move] = EMPTY
    #  поскольку следующим ходом  ни  одна  сторона  не  может  победить.
    #  выберем лучшее из  доступных  полей
    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move



def check():
    if board['T1'] == 'X' and board['T2'] == 'X' and board['T3'] == 'X':
        print('Первый игрок победил!')
        return 1
    if board['M1'] == 'X' and board['M2'] == 'X' and board['M3'] == 'X':
        print('Первый игрок победил!!')
        return 1
    if board['D1'] == 'X' and board['D2'] == 'X' and board['D3'] == 'X':
        print('Первый игрок победил!!')
        return 1

    if board['T1'] == 'X' and board['M2'] == 'X' and board['D3'] == 'X':
        print('Первый игрок победил!!')
        return 1

    if board['T3'] == 'X' and board['M2'] == 'X' and board['D1'] == 'X':
        print('Первый игрок победил!!')
        return 1

    if board['T1'] == 'X' and board['M1'] == 'X' and board['D1'] == 'X':
        print('Первый игрок победил!')
        return 1
    if board['T2'] == 'X' and board['M2'] == 'X' and board['D2'] == 'X':
        print('Первый игрок победил!!')
        return 1
    if board['T3'] == 'X' and board['M3'] == 'X' and board['D3'] == 'X':
        print('Первый игрок победил!!')
        return 1

    if board['T1'] == 'O' and board['T2'] == 'O' and board['T3'] == 'O':
        print('Второй игрок победил!!')
        return 1
    if board['M1'] == 'O' and board['M2'] == 'O' and board['M3'] == 'O':
        print('Второй игрок победил!!')
        return 1
    if board['D1'] == 'O' and board['D2'] == 'O' and board['D3'] == 'O':
        print('Второй игрок победил!!')
        return 1
    if board['T1'] == 'O' and board['M2'] == 'O' and board['D3'] == 'O':
        print('Второй игрок победил!!')
        return 1
    if board['T1'] == 'O' and board['M1'] == 'O' and board['D1'] == 'O':
        print('Второй игрок победил!')
        return 1
    if board['T2'] == 'O' and board['M2'] == 'O' and board['D2'] == 'O':
        print('Второй игрок победил!')
        return 1
    if board['T3'] == 'O' and board['M3'] == 'O' and board['D3'] == 'O':
        print('Второй игрок победил!!')
        return 1
    return 0

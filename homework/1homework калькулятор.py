positions= ['' for i in range(9)]
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


def computer_move(human):
    human_list = []
    for i in positions:
        if i == human:
            human_list.append(i)
    if computer_move == [4]:
        return "4"
    for j in win_positions:
        human_set = set(human_list)
        win_set = set(j)
        w_s = win_set & human_set
        if len(w_s) == 2:
            return






def is_winner(bo, le):
                return (bo[7] == le and bo[8] == le and bo[9] == le) or \
                       (bo[4] == le and bo[5] == le and bo[6] == le) or \
                       (bo[1] == le and bo[2] == le and bo[3] == le) or \
                       (bo[1] == le and bo[4] == le and bo[7] == le) or \
                       (bo[2] == le and bo[5] == le and bo[8] == le) or \
                       (bo[3] == le and bo[6] == le and bo[9] == le) or \
                       (bo[1] == le and bo[5] == le and bo[9] == le) or \
                       (bo[3] == le and bo[5] == le and bo[7] == le)

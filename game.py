import random

BOARD_SIZE = 7
FINISH_LINE = BOARD_SIZE ** 2
CELL_SIZE = 5

positions = [0, 0]
player = 0
winner = None
die = None

def draw_horizontal_line():
    print('+' + '-' * (CELL_SIZE * BOARD_SIZE - 1)  + '+')

def draw_row(row_index):
    row = '|'
    for column in range(BOARD_SIZE):
        cell = row_index * BOARD_SIZE + column + 1
        if positions[0] == cell:
            if positions[1] == cell:
                row += ' X+ '
            else:
                row += ' X  '
        elif positions[1] == cell:
            row += '  + '
        else:
            row += f"{cell:=3} "
        row += '|'
    print(row)

def draw_board():
    draw_horizontal_line()
    for line in reversed(range(BOARD_SIZE)):
        draw_row(line)
        draw_horizontal_line()

def wait():
    input("Press Enter to continue...")

def roll():
    global die
    global player
    global positions
    die = random.randint(1, 6)    
    print(f"Player {player+1} rolled a {die}")
    positions[player] += die
    # print(positions)
    if positions[player] > FINISH_LINE:
        print(f"Player {player+1} wins!")
        exit(0)
    player = 1 - player

while winner is None:
    draw_board()
    wait()
    roll()

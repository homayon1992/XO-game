m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 1


def winner():
    return False


def board_is_full(): 
    for row in m:
        for value in row:
            if value == ' ':
                return False
    return True


def show_board():
    for row in m:
        print("-" * 10)
        for value in row:
            print("|",value, end="")
        print("|")
    print("-"*10)


def get_input():
    row = int(input('enter row number '))
    col = int(input('enter col number '))
    m[row][col] = 'X' if player == 1 else 'O'

def change_player():
    global player
    player = player % 2+1



if __name__ == '__main__':
    while(winner()==False and board_is_full()==False) :
        show_board()
        get_input()
        change_player()
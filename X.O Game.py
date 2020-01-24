m = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
player = 1


def winner():
        if (m[0][0] == 'X' and m[0][1] == 'X' and m[0][2] == 'X') or \
                (m[1][0] == 'X' and m[1][1] == 'X' and m[1][2] == 'X') or \
                (m[2][0] == 'X' and m[2][1] == 'X' and m[2][2] == 'X') or \
                (m[0][0] == 'X' and m[1][0] == 'X' and m[2][0] == 'X') or \
                (m[0][1] == 'X' and m[1][1] == 'X' and m[2][1] == 'X') or \
                (m[0][2] == 'X' and m[1][2] == 'X' and m[2][2] == 'X') or \
                (m[0][0] == 'X' and m[1][1] == 'X' and m[2][2] == 'X') or \
                (m[0][2] == 'X' and m[1][1] == 'X' and m[2][0] == 'X'):
            print("X is winner!")
            return True
        if (m[0][0] == 'O' and m[0][1] == 'O' and m[0][2] == 'O') or \
                (m[1][0] == 'O' and m[1][1] == 'O' and m[1][2] == 'O') or \
                (m[2][0] == 'O' and m[2][1] == 'O' and m[2][2] == 'O') or \
                (m[0][0] == 'O' and m[1][0] == 'O' and m[2][0] == 'O') or \
                (m[0][1] == 'O' and m[1][1] == 'O' and m[2][1] == 'O') or \
                (m[0][2] == 'O' and m[1][2] == 'O' and m[2][2] == 'O') or \
                (m[0][0] == 'O' and m[1][1] == 'O' and m[2][2] == 'O') or \
                (m[0][2] == 'O' and m[1][1] == 'O' and m[2][0] == 'O'):
            print("O is winner!")
            return True

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
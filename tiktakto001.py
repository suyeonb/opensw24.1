board = [[' ' for x in range(3)] for y in range(3)]

def print_board(board):
    for r in range(3):
        print(" " + board[r][0] + "| " + board[r][1] + "| " + board[r][2])
        if r != 2:
            print("---|---|---")

def check_winner(board):
    # 가로, 세로, 대각선 방향을 검사하여 승자가 있는지 확인
    # 가로 방향
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]
    # 세로 방향
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    # 대각선 방향
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

print("게임을 시작합니다.")
print_board(board)

while True:
    # 사용자가 좌표를 입력
    while True:
        x = int(input("다음 수의 x좌표를 입력하시오: "))
        y = int(input("다음 수의 y좌표를 입력하시오: "))

        if board[x][y] == ' ':
            board[x][y] = 'X'
            break
        else:
            print("잘못된 위치입니다.")

    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner}가 이겼습니다!")
        break
    elif is_board_full(board):
        print("무승부입니다!")
        break

    # 컴퓨터의 좌표
    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                break
        else:
            continue
        break

    print("컴퓨터가 수를 두었습니다.")
    print_board(board)
    winner = check_winner(board)
    if winner:
        print(f"{winner}가 이겼습니다!")
        break
    elif is_board_full(board):
        print("무승부입니다!")
        break
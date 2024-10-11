def is_in_check(board):
    king_position = None
    
   
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 'K':
                king_position = (i, j)
                break
        if king_position:
            break

    if not king_position:
        print("Error: King not found")
        return

    king_x, king_y = king_position
    board_size = len(board)

   
    directions = {
        'rook': [(1, 0), (-1, 0), (0, 1), (0, -1)],
        'bishop': [(1, 1), (1, -1), (-1, 1), (-1, -1)]  
    }

    
    for dx, dy in directions['rook']:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < board_size and 0 <= y < board_size:
            if board[x][y] == 'R' or board[x][y] == 'Q':
                print("Success")
                return
            if board[x][y] != '.':
                break
            x += dx
            y += dy

    
    for dx, dy in directions['bishop']:
        x, y = king_x + dx, king_y + dy
        while 0 <= x < board_size and 0 <= y < board_size:
            if board[x][y] == 'B' or board[x][y] == 'Q':
                print("Success")
                return
            if board[x][y] != '.':
                break
            x += dx
            y += dy

    
    knight_moves = [
        (2, 1), (2, -1), (-2, 1), (-2, -1),
        (1, 2), (1, -2), (-1, 2), (-1, -2)
    ]
    
    for dx, dy in knight_moves:
        x, y = king_x + dx, king_y + dy
        if 0 <= x < board_size and 0 <= y < board_size:
            if board[x][y] == 'N':
                print("Success")
                return

    
    pawn_attacks = [(1, -1), (1, 1)]  
    for dx, dy in pawn_attacks:
        x, y = king_x + dx, king_y + dy
        if 0 <= x < board_size and 0 <= y < board_size:
            if board[x][y] == 'P':
                print("Success")
                return

 
    print("Fail")

if __name__ == "__main__":
   
    chess_board = [
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', 'K', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['P', '.', '.', '.', '.', 'B', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', 'R'],
    ]
    
    is_in_check(chess_board)
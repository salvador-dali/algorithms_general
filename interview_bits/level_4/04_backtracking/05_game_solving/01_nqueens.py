# https://www.interviewbit.com/problems/nqueens/
def put_queen(board, y, x):
    M = [i[::] for i in board]
    n, M[y][x] = len(M), 2
    for i in xrange(n):
        M[y][i] = 1 if not M[y][i] else M[y][i]

    for i in xrange(len(M)):
        M[i][x] = 1 if not M[i][x] else M[i][x]

    cur_y, cur_x = y + 1, x + 1
    while cur_y < n and cur_x < n:
        M[cur_y][cur_x] = 1 if not M[cur_y][cur_x] else M[cur_y][cur_x]
        cur_y, cur_x = cur_y + 1, cur_x + 1

    cur_y, cur_x = y + 1, x - 1
    while cur_y < n and cur_x >= 0:
        M[cur_y][cur_x] = 1 if not M[cur_y][cur_x] else M[cur_y][cur_x]
        cur_y, cur_x = cur_y + 1, cur_x - 1

    cur_y, cur_x = y - 1, x - 1
    while cur_y >= 0 and cur_x >= 0:
        M[cur_y][cur_x] = 1 if not M[cur_y][cur_x] else M[cur_y][cur_x]
        cur_y, cur_x = cur_y - 1, cur_x - 1

    cur_y, cur_x = y - 1, x + 1
    while cur_y >= 0 and cur_x < n:
        M[cur_y][cur_x] = 1 if not M[cur_y][cur_x] else M[cur_y][cur_x]
        cur_y, cur_x = cur_y - 1, cur_x + 1

    return M

def early_prune(board):
    empty_cols, empty_rows, left_queens = set([]), set([]), len(board)
    for y in xrange(len(board)):
        for x in xrange(len(board)):
            if board[y][x] == 2:
                left_queens -= 1
            elif board[y][x] == 0:
                empty_cols.add(x)
                empty_rows.add(y)

    if left_queens > len(empty_cols) or left_queens > len(empty_rows):
        return True
    return False

def convert_board(board):
    return [''.join(['Q' if el == 2 else '.' for el in line]) for line in board]

def final_solution(n):
    def generate_all_queens(board, curr_queen_number):
        tuple_from_board, n = tuple(tuple(i) for i in board), len(board)
        if tuple_from_board in seen_positions:
            return

        seen_positions.add(tuple_from_board)
        if early_prune(board):
            return
        if curr_queen_number == n:
            results.add(tuple(tuple(i) for i in board))
            return

        for y in xrange(n):
            for x in xrange(n):
                if not board[y][x]:
                    generate_all_queens(put_queen(board, y, x), curr_queen_number + 1)

    seen_positions, results = set([]), set([])
    M = [[0 for i in xrange(n)] for j in xrange(n)]
    generate_all_queens(M, 0)

    return [convert_board(board) for board in results]


# not my solution
# http://rosettacode.org/wiki/N-queens_problem#Python

from itertools import permutations

def board(vec, n):
    return ['.' * i + 'Q' + '.' * (n-i-1) for i in vec]

def generate_all(n):
    cols, res = range(n), []
    for vec in permutations(cols):
        if n == len(set(vec[i]+i for i in cols)) == len(set(vec[i]-i for i in cols)):
            res.append(board(vec, n))

    return res


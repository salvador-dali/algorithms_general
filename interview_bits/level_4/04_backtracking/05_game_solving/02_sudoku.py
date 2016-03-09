# https://www.interviewbit.com/problems/sudoku/
from copy import deepcopy

def get_starting_possible(M):
    full_set = set(range(1, 10))
    possible_in_rows = [full_set - {i for i in line if i} for line in M]
    possible_in_cols = [set(range(1, 10)) for i in xrange(9)]

    for line in M:
        for pos, num in enumerate(line):
            if num:
                possible_in_cols[pos].discard(num)

    possible_in_squares = [
        full_set - ({M[0][i] for i in xrange(0, 3)} | {M[1][i] for i in xrange(0, 3)} | {M[2][i] for i in xrange(0, 3)}),
        full_set - ({M[0][i] for i in xrange(3, 6)} | {M[1][i] for i in xrange(3, 6)} | {M[2][i] for i in xrange(3, 6)}),
        full_set - ({M[0][i] for i in xrange(6, 9)} | {M[1][i] for i in xrange(6, 9)} | {M[2][i] for i in xrange(6, 9)}),
        full_set - ({M[3][i] for i in xrange(0, 3)} | {M[4][i] for i in xrange(0, 3)} | {M[5][i] for i in xrange(0, 3)}),
        full_set - ({M[3][i] for i in xrange(3, 6)} | {M[4][i] for i in xrange(3, 6)} | {M[5][i] for i in xrange(3, 6)}),
        full_set - ({M[3][i] for i in xrange(6, 9)} | {M[4][i] for i in xrange(6, 9)} | {M[5][i] for i in xrange(6, 9)}),
        full_set - ({M[6][i] for i in xrange(0, 3)} | {M[7][i] for i in xrange(0, 3)} | {M[8][i] for i in xrange(0, 3)}),
        full_set - ({M[6][i] for i in xrange(3, 6)} | {M[7][i] for i in xrange(3, 6)} | {M[8][i] for i in xrange(3, 6)}),
        full_set - ({M[6][i] for i in xrange(6, 9)} | {M[7][i] for i in xrange(6, 9)} | {M[8][i] for i in xrange(6, 9)})
    ]
    return possible_in_rows, possible_in_cols, possible_in_squares

def solve(M):
    res = []
    def recursive_search(M, p_rows, p_cols, p_sqrs, zeros):
        if not zeros:
            res.append(M)
            return

        row, col = zeros.pop()
        sqr = row / 3 * 3 + col / 3

        possible = p_rows[row] & p_cols[col] & p_sqrs[sqr]
        for new_val in possible:
            M_, p_rows_, p_cols_, p_sqrs_, zeros_ = deepcopy(M), deepcopy(p_rows), deepcopy(p_cols), deepcopy(p_sqrs), deepcopy(zeros)
            p_rows_[row].discard(new_val)
            p_cols_[col].discard(new_val)
            p_sqrs_[sqr].discard(new_val)
            M_[row][col] = new_val
            recursive_search(M_, p_rows_, p_cols_, p_sqrs_, zeros_)

    (p_rows, p_cols, p_sqrs), zeros = get_starting_possible(M), []
    for i, line in enumerate(M):
        for j, el in enumerate(line):
            if el == 0:
                zeros.append((i, j))

    recursive_search(M, p_rows, p_cols, p_sqrs, zeros)
    return res.pop()

arr = ["53..7....", "6..195...", ".98....6.", "8...6...3", "4..8.3..1", "7...2...6", ".6....28.", "...419..5", "....8..79"]
M = [[int(i) if i != '.' else 0 for i in line] for line in arr]
print [''.join(map(str, i)) for i in solve(M)]

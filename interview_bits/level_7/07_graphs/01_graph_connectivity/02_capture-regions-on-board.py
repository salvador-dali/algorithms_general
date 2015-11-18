# https://www.interviewbit.com/problems/capture-regions-on-board/
def capture_if_needed(M, i, j):
    have_seen, frontier, should_be_captured = set(), [(i, j)], True
    while frontier:
        y, x = frontier.pop()
        have_seen.add((y, x))
        if x == 0 or y == 0 or x == len(M[0]) - 1 or y == len(M) - 1:
            should_be_captured = False

        for y1, x1 in [(y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)]:
            if 0 <= x1 < len(M[0]) and 0 <= y1 < len(M) and M[y1][x1] == 'O' and (y1, x1) not in have_seen:
                frontier.append((y1, x1))

    how_to_mark = 'X' if should_be_captured else '-'
    for y, x in have_seen:
        M[y][x] = how_to_mark

def capturing(M):
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if M[i][j] == 'O':
                capture_if_needed(M, i, j)

    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            M[i][j] = 'X' if M[i][j] == 'X' else 'O'
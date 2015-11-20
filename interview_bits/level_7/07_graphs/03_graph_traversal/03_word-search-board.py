# https://www.interviewbit.com/problems/word-search-board/
def can_construct(M, word):
    if not word:
        return True

    frontier = []
    for i in xrange(len(M)):
        for j in xrange(len(M[0])):
            if M[i][j] == word[0]:
                frontier.append((i, j, 0))

    while frontier:
        y, x, pos = frontier.pop()
        for y1, x1 in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if 0 <= y1 < len(M) and 0 <= x1 < len(M[0]) and M[y1][x1] == word[pos + 1]:
                frontier.append((y1, x1, pos + 1))
                if pos + 2 == len(word):
                    return True

    return False

can_construct(["FEDCBECD", "FABBGACG", "CDEDGAEC", "BFFEGGBA", "FCEEAFDA", "AGFADEAC", "ADGDCBAA", "EAABDDFF"], 'BCDCB')
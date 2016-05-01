def getSolution(moves):
    move = moves[0]
    prevPositions = {(move[1], -1): abs(move[1] - move[0])}
    for move in moves[1:]:
        newPositions = {}
        for pos in prevPositions:
            el1, val1 = (move[1], pos[1]), prevPositions[pos] + abs(pos[0] - move[0]) + abs(move[0] - move[1])
            newPositions[el1] = min(newPositions.get(el1, float('inf')), val1)

            el2 = (pos[0], move[1])
            if pos[1] == -1:
                val2 = prevPositions[pos] + abs(move[0] - move[1])
            else:
                val2 = prevPositions[pos] + abs(pos[1] - move[0]) + abs(move[0] - move[1])

            newPositions[el2] = min(newPositions.get(el2, float('inf')), val2)

        prevPositions = newPositions

    return min(prevPositions.values())

def getSolution2(moves):
    move = moves[0]
    prevPositions = {(move[1], -1): abs(move[1] - move[0])}
    for move in moves[1:]:
        newPositions = {}
        for pos in prevPositions:
            el1, val1 = (move[1], pos[1]), prevPositions[pos] + abs(pos[0] - move[0]) + abs(move[0] - move[1])
            newPositions[el1] = min(newPositions.get(el1, float('inf')), val1)

            el2 = (pos[0], move[1])
            if pos[1] == -1:
                val2 = prevPositions[pos] + abs(move[0] - move[1])
            else:
                val2 = prevPositions[pos] + abs(pos[1] - move[0]) + abs(move[0] - move[1])

            newPositions[el2] = min(newPositions.get(el2, float('inf')), val2)

        prevPositions = newPositions

    return min(prevPositions.values())

def DP(q, n, moves):
    F = []
    for i in xrange(q):
        F.append([9] * n)

    # Let f(i, j) be the minimum travel distance required to perform the first i trips, and
    # which leaves one car at City dest[i] and the other at City j.

    # The first option will cost f(i-1, j) + |dest[i-1]-a| + |b-a|, while the second
    # will cost f(i-1, a) + |b-a| + |dest[i-1]-j|

    for i in F:
        print i

M, N, moves = 5, 4, [(1, 5), (3, 2), (4, 1), (2, 4)]
# M, N, moves = 4, 2, [(1, 2), (4, 3)]

print getSolution(moves)
DP(N, M, moves)

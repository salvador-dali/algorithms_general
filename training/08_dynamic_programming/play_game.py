# https://www.hackerrank.com/challenges/play-game
# suppose the numbers are
# 6, 8, 1, 1, 6 and their positions
# 0, 1, 2, 3, 4
# looking at them from the reverse order, one can see that if we are now in the position 4,
# the best play is to grab 6, in position 3 then 1 + 6, position 2 - then 1 + 1 + 6.
# In all the cases the opponent will have 0
# if we are in position 1, then we can take:
# only 8 which means that our opponent will take the best for him (all values and gives use 0)
# we will populate our DP table in reverse order where keys are positions and
# values - are [competitorBestScore, yourBestScore]
def playGame(arr):
    l = len(arr)
    if l < 4:
        return sum(arr)

    bestScore = {
        l - 1: [arr[l - 1], 0],
        l - 2: [arr[l - 1] + arr[l - 2], 0],
        l - 3: [arr[l - 1] + arr[l - 2] + arr[l - 3], 0]
    }
    for i in xrange(3, l):
        pos = l - i - 1
        ways = [[sum(arr[pos:pos + i]) + bestScore[pos + i][1], bestScore[pos + i][0]] for i in xrange(1, 4)]
        best = sorted(ways, key=lambda x: -x[0])
        bestScore[pos] = best[0]

    return bestScore[0]

for i in xrange(input()):
    raw_input()
    print playGame(map(int, raw_input()))[0]
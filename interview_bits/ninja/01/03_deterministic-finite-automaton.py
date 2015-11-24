# https://www.interviewbit.com/problems/deterministic-finite-automaton
from collections import defaultdict

def DFA(jump_0, jump_1, start, end_arr, n):
    dp = [[0] * len(jump_0) for _ in xrange(n + 1)]
    m = defaultdict(list)
    for s, e in enumerate(jump_0):
        m[e].append(s)

    for s, e in enumerate(jump_1):
        m[e].append(s)

    for i in end_arr:
        dp[0][i] = 1

    for i in xrange(1, n + 1):
        for j in xrange(len(jump_0)):
            dp[i][j] = sum(dp[i - 1][el] for el in m[j]) % (10**9 + 7)

    return dp[-1][start]

jump_0 = [0, 2, 1]
jump_1 = [1, 0, 2]
start = 1
end = [0]
DFA(jump_0, jump_1, start, end, 80)
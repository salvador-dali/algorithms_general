# https://www.hackerrank.com/contests/worldcodesprint/challenges/save-our-ship
S, total = raw_input().strip(), 0
for i in xrange(len(S)):
    if i % 3 == 1:
        if S[i] != 'O':
            total += 1
    elif S[i] != 'S':
        total += 1


print total

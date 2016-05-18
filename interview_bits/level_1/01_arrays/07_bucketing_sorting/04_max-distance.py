# https://www.interviewbit.com/problems/max-distance/
arr = [3, 2, 5, 4]
def notsurewhattonamethis(A):
    S = [0]
    for i,v in enumerate(A):
        if v<A[S[-1]]:
            S.append(i)
    best = (-1,-1)
    for i,v in reversed(list(enumerate(A))):
        while v>A[S[-1]]:
            j = S.pop()
            d = i - j
            if d > best[1]-best[0]:
                best = (j,i)
            if not S: return best
    return best

print notsurewhattonamethis(arr)
# https://www.interviewbit.com/problems/jump-game-array/
def can_reach(arr):
    best_dist = 0
    for i in xrange(len(arr) - 1):
        best_dist = max(best_dist, i + arr[i])
        if best_dist == i:
            return False

    return True
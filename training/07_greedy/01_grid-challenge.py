# https://www.hackerrank.com/domains/algorithms/greedy
def grid_challenge(arr):
    modified = [sorted(i) for i in arr]
    for i in xrange(len(modified[0])):
        prev = 'a'
        for j in xrange(len(modified)):
            current = modified[j][i]
            if current < prev:
                return False

            prev = current

    return True

for _ in xrange(int(raw_input())):
    num = int(raw_input())
    arr = [raw_input() for i in xrange(num)]
    print 'YES' if grid_challenge(arr) else 'NO'
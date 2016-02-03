# https://www.interviewbit.com/problems/colorful-number/
def isColorful(n):
    arr, seen = map(int, list(str(n))), set([])
    for i in xrange(len(arr)):
        prev = arr[i]
        if prev in seen:
            return 0
        seen.add(prev)
        for j in xrange(i + 1, len(arr)):
            prev *= arr[j]
            if prev in seen:
                return 0
            seen.add(prev)

    return 1

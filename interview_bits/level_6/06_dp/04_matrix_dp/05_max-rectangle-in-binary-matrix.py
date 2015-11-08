# https://www.interviewbit.com/problems/max-rectangle-in-binary-matrix/
def largest_rect(arr):
    stack, maximum, pos = [], 0, 0
    for pos, height in enumerate(arr):
        start = pos
        while True:
            if not stack or stack[-1][1] < height:
                stack.append((start, height))
                break

            maximum = max(maximum, stack[-1][1] * (pos - stack[-1][0]))
            start, _ = stack.pop()

    pos += 1
    for start, height in stack:
        maximum = max(maximum, height * (pos - start))

    return maximum

def largest_matrix(arr):
    for i in xrange(1, len(arr)):
        for j in xrange(len(arr[0])):
            if arr[i][j]:
                arr[i][j] = 1 + arr[i - 1][j]

    return max(largest_rect(i) for i in arr)





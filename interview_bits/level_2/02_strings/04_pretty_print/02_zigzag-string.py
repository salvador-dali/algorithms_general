# https://www.interviewbit.com/problems/zigzag-string/
def zigzag(s, n):
    if n == 1:
        return s
    lines = [''] * n
    lineNum, direction = 0, 1
    for i in s:
        lines[lineNum] += i
        lineNum += direction
        if lineNum == n - 1:
            direction = -1
        elif lineNum == 0:
            direction = 1

    return ''.join(lines)

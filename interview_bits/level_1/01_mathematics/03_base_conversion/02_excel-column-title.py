# https://www.interviewbit.com/problems/excel-column-title/
def excel(n):
    s = []
    while n:
        n -= 1
        s.append(chr(n % 26 + 65))
        n /= 26

    return ''.join(s[::-1])

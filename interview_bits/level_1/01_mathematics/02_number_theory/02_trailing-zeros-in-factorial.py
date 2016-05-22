# https://www.interviewbit.com/problems/trailing-zeros-in-factorial/
def trailing(n):
    s, d = 0, 5
    while n / d:
        s += n / d
        d *= 5
    return s
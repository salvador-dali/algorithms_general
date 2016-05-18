# https://www.interviewbit.com/problems/reverse-integer/
def rev(n):
    sign = -1 if n < 0 else 1
    r = str(abs(n))[::-1]
    val = sign * int(r)
    if -2147483648 <= val <= 2147483647:
        return val
    return 0


# https://www.interviewbit.com/problems/binary-representation/
def binary(n):
    if n == 0:
        return '0'
    arr = []
    while n:
        arr.append(str(n % 2))
        n /= 2

    return ''.join(arr[::-1])
# https://www.interviewbit.com/problems/reverse-bits/
def reverseBits(n):
    arr = []
    while n:
        arr.append(n % 2)
        n /= 2

    arr = arr + [0] * (32 - len(arr))
    num, mul = 0, 1
    for i in arr[::-1]:
        num += i * mul
        mul *= 2
    return num

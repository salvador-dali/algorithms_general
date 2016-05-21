# https://www.interviewbit.com/problems/excel-column-number/
def strToNum(s):
    total, mul = 0, 1
    for i in s[::-1]:
        total += (ord(i) - 64) * mul
        mul *= 26
    return total

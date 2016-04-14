# https://www.interviewbit.com/problems/integer-to-roman/

def integer2roman(n):
    possible = [
        (1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
        (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')
    ]
    res = ''
    while n:
        for val, key in possible:
            if val <= n:
                n -= val
                res += key
                break
    return res


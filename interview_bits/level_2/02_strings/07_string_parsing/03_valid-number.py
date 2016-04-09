# https://www.interviewbit.com/problems/valid-number/
def isNumber(A):
    A = A.strip()
    if len(A) == 0:
        return 0
    digits = "1234567890.-"
    if 'e' in A:
        index = A.index('e')
        base, exp = A[:index], A[index+1:]
    else:
        base, exp = A, ''
    if '.' in exp or base[-1] == '.':
        return 0
    if base.count('-') > 1 or (base.count('-') == 1 and base[0] != '-') or base.count('.') > 1:
        return 0
    if exp.count('-') > 1 or (exp.count('-') == 1 and exp[0] != '-'):
        return 0
    for char in base:
        if char not in digits:
            return 0
    for char in exp:
        if char not in digits:
            return 0
    return 1
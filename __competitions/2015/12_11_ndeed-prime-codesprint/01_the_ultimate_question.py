# https://www.hackerrank.com/contests/indeed-prime-codesprint/challenges/the-ultimate-question
a, b, c = raw_input().split()

def func(a, b, c):
    attempts = [
        ['+', '+'],
        ['+', '*'],
        ['*', '+'],
        ['*', '*'],
    ]
    for i in attempts:
        if eval(a + i[0] + b + i[1] + c) == 42:
            return a + i[0] + b + i[1] + c
    return 'This is not the ultimate question'

print func(a, b, c)
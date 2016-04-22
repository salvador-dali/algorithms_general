# https://www.hackerrank.com/challenges/chocolate-feast
def getChocolates(a, b, c):
    chocolate = a / b
    wrappers = chocolate

    while wrappers / c:
        newChocolate = wrappers / c
        chocolate += newChocolate
        wrappers = wrappers % c + newChocolate

    return chocolate


for i in range(input()):
    a, b, c = map(int, raw_input().split())
    print getChocolates(a, b, c)
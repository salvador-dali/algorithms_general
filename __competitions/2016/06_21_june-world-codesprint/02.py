raw_input()

a1 = map(int, raw_input().split())[::-1]
a2 = map(int, raw_input().split())[::-1]
a3 = map(int, raw_input().split())[::-1]

def cumSumSet(a1):
    s, cum = 0, set()
    for i in a1:
        s += i
        cum.add(s)

    return cum

def findAll(a1, a2, a3):
    res = cumSumSet(a1) & cumSumSet(a2) & cumSumSet(a3)
    if len(res) == 0:
        return 0
    return max(res)

findAll(a1, a2, a3)
# https://www.hackerrank.com/challenges/alternating-characters
def alternate(el):
    prev, num = 'C', 0
    for i in el:
        if prev == i:
            num += 1

        prev = i

    return num

for i in xrange(input()):
    print alternate(raw_input())
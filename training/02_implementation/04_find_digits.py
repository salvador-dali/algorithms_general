# https://www.hackerrank.com/challenges/find-digits
def stupidity(n):
    hash = {}
    for i in range(1, 10):
        if not n % i:
            hash[i] = 1

    num = 0
    for i in str(n):
        if int(i) in hash:
            num += 1

    return num

for i in xrange(input()):
    print stupidity(input())
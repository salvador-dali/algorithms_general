def analyse(C, M, n):
    multiplier = C**2 % M
    if n == 1:
        return 0
    if n == 2:
        return len([(13 % M * multiplier) % M])

    arr = [13 % M, 34 % M]
    for i in xrange(2 * n - 5):
        arr.append((3 * arr[-1] - arr[-2]) % M)

    return len(set([i * multiplier % M for i in set(arr)]))

from random import randint
from datetime import datetime
startTime = datetime.now()
C, M, n = randint(10**7, 10**8), randint(10**7, 10**8), randint(10**6, 2 * 10**6)
print analyse(C, M, n)
print datetime.now() - startTime
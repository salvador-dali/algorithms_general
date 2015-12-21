# better brute
MOD = 10**9 + 7
def update_row(r, d):
    s = d
    for i in xrange(N - r, N - r + M):
        diagonals[i] = (diagonals[i] + s) % MOD
        s = (s + d) % MOD

def update_col(c, d):
    s = d
    for i in xrange(N):
        diagonals[N + c - 2 - i] = (diagonals[N + c - 2 - i] + s) % MOD
        s = (s + d) % MOD

def update_reg(x1, y1, x2, y2, d):
    s = y1 - 1 + N - x2
    e = y2 - 1 + N - x1
    size = min(y2 - y1 + 1, x2 - x1 + 1)

    number = size * d
    for i in xrange(s, e + 1):
        diagonals[i] = (diagonals[i] + number) % MOD

    number -= d
    for i in xrange(1, size):
        diagonals[s + i - 1] = (diagonals[s + i - 1] - number) % MOD
        diagonals[e - i + 1] = (diagonals[e - i + 1] - number) % MOD
        number -= d

def getSum(a, b):
    s = 0
    for i in xrange(a - 1, b):
        s = (s + diagonals[i]) % MOD

    print s % MOD

N, M, Q = map(int, raw_input().split())
diagonals = [0] * (N + M - 1)

for i in xrange(Q):
    arr = raw_input().split()
    t, a, b = arr[0], int(arr[1]), int(arr[2])
    if t == 'Qd':
        getSum(a, b)
    elif t == 'Qr':
        update_row(a, b)
    elif t == 'Qc':
        update_col(a, b)
    else:
        update_reg(a, b, int(arr[3]), int(arr[4]), int(arr[5]))
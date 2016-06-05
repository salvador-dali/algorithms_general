def get_divisor_sieve(n):
    p, n_sqrt, sieve = 3, int(n**0.5) + 1, [0] * (n + 1)

    for i in range(2, n + 1, 2):
        sieve[i] = 2

    while p <= n_sqrt:
        for i in xrange(p, n + 1, p):
            if not sieve[i]:
                sieve[i] = p

        while p < len(sieve) and sieve[p]:
            p += 2
    while p < n + 1:
        if not sieve[p]:
            sieve[p] = p
        p += 2

    return sieve

def get_divisors_from_sieve(divisor_sieve, num):
    divisors = []
    while num > 1:
        divisors.append(divisor_sieve[num])
        num /= divisor_sieve[num]

    return divisors

def get_factors_num(numbers):
    sieve = get_divisor_sieve(max(numbers))
    return [len(get_divisors_from_sieve(sieve, i)) for i in numbers]


all_values, questions = [], []
for i in xrange(input()):
    input()
    arr = map(int, raw_input().split())
    all_values += arr
    questions.append(arr)
    
all_values = list(set(all_values))
factors = get_factors_num(all_values)
d = {k: v for k, v in zip(all_values, factors)}

for q in questions:
    res = 0
    for i in q:
        res ^= d[i]
    print 1 if res != 0 else 2
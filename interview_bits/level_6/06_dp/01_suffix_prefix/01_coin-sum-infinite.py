# https://www.interviewbit.com/problems/coin-sum-infinite/
def memoid(n, numbers):
    memo = {}
    def coin_sum(n, numbers):
        if (n, tuple(numbers)) in memo:
            return memo[(n, tuple(numbers))]

        if n < 0:
            return 0
        if n == 0:
            return 1

        if len(numbers) == 0:
            return 0

        val = (coin_sum(n - numbers[0], numbers) + coin_sum(n, numbers[1:])) % 1000007
        memo[(n, tuple(numbers))] = val
        return val

    res = coin_sum(n, numbers)
    return res

def coinChange(n, coins):
    coins.sort()
    counts = [1] + [0] * n
    for c in coins:
        for i in range(len(counts)):
            if c + i <= n:
                counts[i + c] = (counts[i] + counts[i + c]) % 1000007

    return counts[-1]
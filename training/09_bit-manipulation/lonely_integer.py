# https://www.hackerrank.com/challenges/lonely-integer
def withoutPair(arr):
    return reduce(lambda x, y: x ^ y, arr)

raw_input()
print withoutPair(list(map(int, raw_input().split())))
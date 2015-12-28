# https://www.hackerrank.com/contests/round-1-holiday-cup/challenges/even-up-solitaire/
n = input()
arr = map(int, raw_input().split())
temp, pos = [0] * n, 0

for i in arr:
    temp[pos] = i % 2
    if pos > 0 and temp[pos] == temp[pos - 1]:
        pos -= 1
    else:
        pos += 1

print pos
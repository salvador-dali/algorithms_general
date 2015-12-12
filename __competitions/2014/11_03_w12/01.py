# https://www.hackerrank.com/contests/w12/challenges/priyanka-and-toys
# sort numbers and use greedy solution to find which one overlap
def toBuy(arr):
    arr.sort()
    num, maxPrice = 0, -1
    for i in arr:
        if i > maxPrice:
            num += 1
            maxPrice = i + 4
    return num

input()
print toBuy(list(map(int, raw_input().split())))


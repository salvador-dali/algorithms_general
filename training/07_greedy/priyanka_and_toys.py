# https://www.hackerrank.com/challenges/priyanka-and-toys
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
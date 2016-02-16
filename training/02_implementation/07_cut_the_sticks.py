# https://www.hackerrank.com/challenges/cut-the-sticks
def cutting(arr):
    while len(arr):
        print len(arr)
        el = arr[0]
        arr = [i - el for i in arr if (i - el)]


raw_input()
arr = list(map(int, raw_input().split()))
arr.sort()

cutting(arr)
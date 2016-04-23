# https://www.hackerrank.com/challenges/insertionsort2
def insertion(arr, el):
    for i in range(len(arr)):
        if el < arr[i]:
            return arr[0:i] + [el] + arr[i:]
    return arr + [el]

def insertionSort(arr):
    l = len(arr)
    for i in range(1, l):
        arr = insertion(arr[0:i], arr[i]) + arr[i + 1:]
        print ' '.join(map(str, arr))

m = input()
insertionSort(map(int, raw_input().split()))
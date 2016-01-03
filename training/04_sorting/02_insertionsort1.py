# https://www.hackerrank.com/challenges/insertionsort1/
def insertionSort(ar):
    n = len(ar)
    v = ar[n - 1]
    for i in range(n-1, 0, -1):
        if ar[i-1] > v:
            ar[i] = ar[i-1]
        else:
            ar[i] = v
            print ' '.join(map(str, ar))
            break
        print ' '.join(map(str, ar))
    if v < ar[0]:
        ar[0] = v
        print ' '.join(map(str, ar))
        
m = input()
insertionSort(map(int, raw_input().split()))
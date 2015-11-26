# https://www.interviewbit.com/problems/min-jumps
arr = [1, 6, 3, 8, 2, -1, 4, 3, -1, 5, -1, 6]
arr = [5, 3, 2, 6, 1, 4, 3, 1]
k = 4

# print str(len(arr)) + ' ' + ' '.join(map(str, arr))
# print k
# print


arr = [1, 3, 4, 1, 6]
def analyze(arr, k):
    dp_cost = [float('inf')] * len(arr)
    dp_prev = [0] * len(arr)
    dp_cost[0] = arr[0]
    dp_prev[0] = -1

    for i in xrange(len(arr) - k + 1):
        for j in xrange(i + 1, i + k):
            prev = -1
            best = float('inf')
            for k in xrange(i, j):
                if dp_cost[k] <= best:
                    best = dp_cost[k]
                    prev = k

            tmp = best + arr[j]


            tmp = min(dp_cost[i:j]) + arr[j]
            dp_cost[j] = min(dp_cost[j], tmp)


    print dp_cost



def analyze2(arr, k):
    dp_cost = [float('inf')] * len(arr)
    dp_prev = [-1] * len(arr)
    dp_cost[0] = arr[0]

    for i in xrange(len(arr) - k + 1):
        for j in xrange(i + 1, i + k):
            min_so_far = float('inf')
            attempt = dp_cost[i] + arr[j]
            if attempt <= min_so_far:
                min_so_far = attempt
                if dp_cost[j] > min_so_far:
                    dp_cost[j] = min_so_far
                    dp_prev[j] = i



    print dp_cost
    print dp_prev



analyze2(arr, k)


# https://www.interviewbit.com/problems/hotel-bookings-possible/

import heapq

def isPossible(arr1, arr2, k):
    arr = [(arr1[i], arr2[i]) for i in xrange(len(arr1)) if arr1[i] != arr2[i]]
    arr.sort()

    queue = []
    for el in arr:
        if len(queue) > k:
            return 0
        if len(queue) == 0:
            heapq.heappush(queue, el[1])
        else:
            num_leave, num_join = queue[0], el[0]
            if num_leave <= num_join:
                heapq.heappushpop(queue, el[1])
            else:
                heapq.heappush(queue, el[1])
    return 0 if len(queue) > k else 1



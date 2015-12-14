def transformWindow(arr):
    r = [0]
    for i in arr:
        if i:
            r[-1] += 1
        elif r[-1]:
            r.append(0)
    return r

def f(n):
    return n * (n + 1) / 2

def middleSum(arr):
    s = 0
    for i in xrange(1, len(arr) - 1):
        s += f(arr[i])

    return s

def anotherTry(arr, k):
    if k == 1:
        for i in xrange(len(arr)):
            print 0
        return
    
    
    l = len(arr)
    asc = [1 if arr[i+1] >= arr[i] else 0 for i in xrange(l - 1)]
    dec = [1 if arr[i+1] <= arr[i] else 0 for i in xrange(l - 1)]

    queue_1 = transformWindow(asc[0:k - 1])
    queue_2 = transformWindow(dec[0:k - 1])
    middleSumNum_1 = middleSum(queue_1)
    middleSumNum_2 = middleSum(queue_2)
    for i in xrange(len(arr) - k + 1):
        first_1 = f(queue_1[0])
        if len(queue_1) > 1:
            last_1 = f(queue_1[-1])
        else:
            last_1 = 0
        win_1 = first_1 + middleSumNum_1 + last_1

        first_2 = f(queue_2[0])
        if len(queue_2) > 1:
            last_2 = f(queue_2[-1])
        else:
            last_2 = 0
        win_2 = first_2 + middleSumNum_2 + last_2
        print win_1 - win_2

        if asc[i]:
            if queue_1[0] == 1:
                if len(queue_1) == 1:
                    queue_1[0] = 0
                else:
                    queue_1.pop(0)
                    if len(queue_1) > 2:
                        middleSumNum_1 -= f(queue_1[0])
                    else:
                        middleSumNum_1 = 0
            else:
                queue_1[0] -= 1

        if dec[i]:
            if queue_2[0] == 1:
                if len(queue_2) == 1:
                    queue_2[0] = 0
                else:
                    queue_2.pop(0)
                    if len(queue_2) > 2:
                        middleSumNum_2 -= f(queue_2[0])
                    else:
                        middleSumNum_2 = 0
            else:
                queue_2[0] -= 1

        if i + k - 1 >= len(asc):
            break
        if asc[i + k - 1]:
            queue_1[-1] += 1
        else:
            if queue_1[-1]:
                if len(queue_1) == 2:
                    middleSumNum_1 = f(queue_1[-1])

                if len(queue_1) > 2:
                    middleSumNum_1 += f(queue_1[-1])

                queue_1.append(0)

        if dec[i + k - 1]:
            queue_2[-1] += 1
        else:
            if queue_2[-1]:
                if len(queue_2) == 2:
                    middleSumNum_2 = f(queue_2[-1])

                if len(queue_2) > 2:
                    middleSumNum_2 += f(queue_2[-1])

                queue_2.append(0)
        
a, k = map(int, raw_input().split())
anotherTry(list(map(int, raw_input().split())), k)
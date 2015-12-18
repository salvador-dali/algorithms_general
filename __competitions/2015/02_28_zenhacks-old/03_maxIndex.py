def getNGE(arr):
    # http://stackoverflow.com/a/19722651/1090562
    stack = [arr[0]]
    for i in xrange(1, len(arr)):
        if len(stack):
            while True:
                if len(stack) == 0 or stack[-1] >= arr[i]:
                    break

                print str(stack.pop()) + ' : ' + str(arr[i])

        stack.append(arr[i])

def getNGI(arr):
    stack = [0]
    h = {}
    for i in xrange(1, len(arr)):
        if len(stack):
            while True:
                if len(stack) == 0 or arr[stack[-1]] >= arr[i]:
                    break

                h[stack.pop()] = i

        stack.append(i)

    res = []
    for i in xrange(len(arr)):
        if i in h:
            res.append(h[i])
        else:
            res.append(-1)

    return res

def getPGI(arr):
    stack = []
    res = []
    for i in xrange(len(arr)):
        while len(stack):
            if arr[stack[-1]] > arr[i]:
                res.append(stack[-1])
                break
            else:
                stack.pop()

        if len(stack) == 0:
            res.append(-1)

        stack.append(i)

    return res

def main(arr):
    a = map(lambda x: x + 1, getNGI(arr))
    b = map(lambda x: x + 1, getPGI(arr))

    maximum = 0
    for i, j in zip(a, b):
        if i * j > maximum:
            maximum = i * j

    return maximum

input()
print main(list(map(int, raw_input().split())))

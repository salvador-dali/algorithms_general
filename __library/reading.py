def test():
    """Basic STDIN, commands"""

    # get Integer from console
    n = input()

    # get two integers from console
    a, b = map(int, raw_input().split())

    # get a list of integers from console
    arr = list(map(int, raw_input().split()))

    # get the list of pairs
    for i in xrange(input()):
        a, b = map(int, raw_input().split())

    # get a list of numbers
    for i in xrange(input()):
        a = input()

    # read from stdin some number of integers separated by newline
    arr = [input() for i in xrange(input())]

    a = [map(int, line.strip().split()) for line in open('file.txt')]
    a = [int(line.strip()) for line in open('file.txt')]


    # check the difference in my solution and correct solution
    test = [map(int, line.strip().split()) for line in open('questions.txt')]
    real = [int(line.strip()) for line in open('answers.txt')]
    for i in xrange(1, len(test)):
        myAns = myFunction(test[i])
        hisAns = real[i - 1]
        if myAns != hisAns:
            print myAns, hisAns

from datetime import datetime
startTime = datetime.now()

print datetime.now() - startTime


from collections import defaultdict

def readGraph():
    graph = defaultdict(set)
    for i in xrange(input() - 1):
        v1, v2 = map(int, raw_input().split())
        graph[v1].add(v2)
        graph[v2].add(v1)

    return dict(graph)
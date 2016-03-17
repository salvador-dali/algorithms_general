# https://www.interviewbit.com/problems/min-stack/

class MinStack:
    def __init__(self):
        self.stack = []
        self.minimum = []

    def printing(self):
        print self.stack
        print self.minimum
        print

    def push(self, x):
        self.stack.append(x)
        self.minimum.append(x if len(self.stack) == 1 else min(x, self.minimum[-1]))

    def pop(self):
        if len(self.stack):
            self.minimum.pop()
            return self.stack.pop()

        return None

    def top(self):
        if len(self.stack):
            return self.stack[-1]

        return -1

    def getMin(self):
        if len(self.stack):
            return self.minimum[-1]

        return -1


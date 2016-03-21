# https://www.interviewbit.com/problems/generate-all-parentheses/
def parenthesis(s):
    data, stack = {')': '(', ']': '[', '}': '{'}, []
    for i in s:
        if i not in data:
            stack.append(i)
        else:
            if not len(stack):
                return False
            if stack.pop() != data[i]:
                return False

    return len(stack) == 0


print parenthesis('{}{}{{()}}{)}(')


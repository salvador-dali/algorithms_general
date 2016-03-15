# https://www.interviewbit.com/problems/evaluate-expression/
def evaluate(arr):
    stack, operators = [], {'+', '-', '/', '*'}
    for i in arr:
        if i in operators:
            b, a = stack.pop(), stack.pop()
            if i == '+':
                res = a + b
            elif i == '*':
                res = a * b
            elif i == '-':
                res = a - b
            else:
                res = a / b

            stack.append(res)
        else:
            stack.append(int(i))

    return stack[-1]
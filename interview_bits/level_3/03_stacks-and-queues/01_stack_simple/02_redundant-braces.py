# https://www.interviewbit.com/problems/redundant-braces/

def redundant(s):
    stack, operators = [], {'+', '*', '-', '/'}
    for i in s:
        if i == '(':
            stack.append('(')
        elif i in operators:
            if len(stack) == 0 or stack[-1] != 'O':
                stack.append('O')
        elif i == ')':
            if len(stack) == 0:
                return True

            if stack[-1] == '(':
                return True

            if stack[-1] == 'O':
                stack.pop()
                if len(stack) == 0:
                    return True
                stack.pop()

    return False


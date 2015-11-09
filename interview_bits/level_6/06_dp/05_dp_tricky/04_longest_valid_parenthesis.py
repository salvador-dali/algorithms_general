# https://www.interviewbit.com/problems/longest-valid-parentheses/
def best_valid(s):
    best_so_far, stack = 0, []
    for i in s:
        # print stack, i
        if i == '(':
            stack.append('(')
        elif i == ')' and stack and stack[-1] == '(':
            stack.pop()
            if stack and type(stack[-1]) == int:
                stack.append(stack.pop() + 1)
            else:
                stack.append(1)
        elif i == ')' and stack and type(stack[-1]) == int:
            num = stack.pop()
            if stack and stack[-1] == '(':
                stack.pop()
                if stack and type(stack[-1]) == int:
                    stack.append(stack.pop() + num + 1)
                else:
                    stack.append(num + 1)
            else:
                best_so_far = max(best_so_far, num)

        # print stack

    for i in stack:
        if type(i) == int:
            best_so_far = max(best_so_far, i)

    return best_so_far * 2


print best_valid('()(()))))')


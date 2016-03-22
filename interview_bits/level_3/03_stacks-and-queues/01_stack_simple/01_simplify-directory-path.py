# https://www.interviewbit.com/problems/simplify-directory-path/

def simplify(s):
    stack = []
    for i in s.split('/'):
        if i == '..':
            if len(stack):
                stack.pop()
        elif i == '' or i == '.':
            pass
        else:
            stack.append(i)

    return '/' + '/'.join(stack)

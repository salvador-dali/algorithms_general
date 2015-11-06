# https://www.interviewbit.com/problems/ways-to-decode/
def find(s):
    if s == '':
        return 1

    if len(s) == 1:
        return 0 if s[0] == '0' else find(s[1:])

    if s[0] == '0':
        return 0
    v1 = find(s[1:])

    if 1 <= int(s[:2]) <= 26:
        v2 = find(s[2:])
    else:
        return v1

    return v1 + v2
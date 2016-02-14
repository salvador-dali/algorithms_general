# https://www.interviewbit.com/problems/fraction/
def fraction(a, b):
    sign, a, b = '-' if a / b < 0 else '', abs(a), abs(b)
    before_point, a, res, seen, pos = str(a / b), a % b, [], {}, 0
    while a:
        if a not in seen:
            seen[a] = pos
            a *= 10
            res.append(str(a / b))
            a %= b
        else:
            break
        pos += 1

    if a not in seen:
        res = before_point + '.' + ''.join(res)
    else:
        res = before_point + '.' + ''.join(res[:seen[a]]) + '(' + ''.join(res[seen[a]:]) + ')'

    if res[-1] == '.':
        return sign + res[:-1]
    return sign + res
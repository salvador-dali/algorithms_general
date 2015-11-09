# https://www.interviewbit.com/problems/evaluate-expression-to-true/

operators = {'|', '&', '^'}
hash_map = {'T': (1, 0), 'F': (0, 1), 'T|T': (1, 0), 'T|F': (1, 0), 'F|T': (1, 0), 'F|F': (0, 1), 'T&T': (1, 0), 'T&F': (0, 1), 'F&T': (0, 1), 'F&F': (0, 1), 'T^T': (0, 1), 'T^F': (1, 0), 'F^T': (1, 0), 'F^F': (0, 1)}

def val(expression, value):
    if expression in hash_map:
        return hash_map[expression][0] if value else hash_map[expression][1]

    res_t, res_f = 0, 0
    for i in xrange(1, len(expression) - 1):
        if expression[i] in operators:
            r, l = expression[:i], expression[i + 1:]
            if expression[i] == '|':
                res_true = val(r, 1) * val(l, 1) + val(r, 1) * val(l, 0) + val(r, 0) * val(l, 1)
                res_false= val(r, 0) * val(l, 0)
            elif expression[i] == '&':
                res_true = val(r, 1) * val(l, 1)
                res_false= val(r, 1) * val(l, 0) + val(r, 0) * val(l, 1) + val(r, 0) * val(l, 0)
            else:
                res_true = val(r, 1) * val(l, 0) + val(r, 0) * val(l, 1)
                res_false= val(r, 1) * val(l, 1) + val(r, 0) * val(l, 0)

            res_t, res_f = res_t + res_true, res_f + res_false


    hash_map[expression] = (res_t, res_f)
    return res_t if value else res_f

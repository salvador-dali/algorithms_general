# generate-all-parentheses-ii
def parentheses(n):
    res = []
    def generate(str):
        if len(str) == 2 * n:
            res.append(str)
            return

        if str.count('(') < n:
            generate(str + '(')

        if str.count(')') < str.count('('):
            generate(str + ')')

    generate('(')
    return res
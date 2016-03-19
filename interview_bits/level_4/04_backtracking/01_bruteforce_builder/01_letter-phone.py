# https://www.interviewbit.com/problems/letter-phone/

data = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
def generate_phones(s):
    if s == '':
        return []
    res = []
    def generate(start, s):
        if len(s) == 0:
            res.append(start)
        else:
            for i in data[int(s[0])]:
                generate(start + i, s[1:])

    generate('', s)
    return res

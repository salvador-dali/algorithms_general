# https://www.hackerrank.com/challenges/pangrams/
def isPangram(s):
    hash = {}
    for i in s.lower():
        if i not in hash:
            hash[i] = 1

    return len(hash) == 27

if isPangram(raw_input()):
    print 'pangram'
else:
    print 'not pangram'
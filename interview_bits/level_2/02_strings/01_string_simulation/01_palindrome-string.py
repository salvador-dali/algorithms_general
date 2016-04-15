# https://www.interviewbit.com/problems/palindrome-string/
def isPalindrome(s):
    if s == '':
        return 1
    p1, p2 = 0, len(s) - 1

    while p1 <= p2:
        while not s[p1].isalnum():
            p1 += 1
            if p1 == len(s):
                return 1

        while not s[p2].isalnum():
            p2 -= 1

        if s[p1].lower() != s[p2].lower():
            return 0

        p1 += 1
        p2 -= 1
    return 1

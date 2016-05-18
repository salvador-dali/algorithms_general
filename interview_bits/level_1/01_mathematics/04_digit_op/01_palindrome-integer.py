# https://www.interviewbit.com/problems/palindrome-integer/
def isPalindrom(n):
    if n < 0:
        return False
    biggest = 1
    while n / biggest:
        biggest *= 10

    biggest /= 10

    while n:
        a, b = n / biggest, n % 10
        if a != b:
            return False
        n = (n - a * biggest) / 10
        biggest /= 100

    return True

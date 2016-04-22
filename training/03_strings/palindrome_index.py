# https://www.hackerrank.com/challenges/palindrome-index/
def isPalindrome(string):
    return string == string[::-1]

def palindrome_index(string):
    start = 0
    end = len(string) - 1

    while start < end:
        if string[start] == string[end]:
            start, end = start+1, end-1
            continue
        if isPalindrome(string[start:end]):
            return end
        else:
            return start
    return -1

for i in xrange(input()):
    print palindrome_index(raw_input())
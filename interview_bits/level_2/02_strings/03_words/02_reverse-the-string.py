# https://www.interviewbit.com/problems/reverse-the-string/

def reverse(s):
    return ' '.join([i[::-1] for i in s[::-1].split()])

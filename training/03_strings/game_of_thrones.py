# https://www.hackerrank.com/challenges/game-of-thrones
def canBePalindrome(s):
    hash = {}
    for i in s:
        if i in hash:
            hash[i]+= 1
        else:
            hash[i] = 1

    tmp = 0
    for i in hash:
        if hash[i] % 2:
            if tmp == 1:
                return False
            else:
                tmp = 1

    return True

if canBePalindrome(raw_input()):
    print("YES")
else:
    print("NO")
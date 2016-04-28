# https://www.hackerrank.com/challenges/counter-game
# if the number is presented in the binary format,
# EX 11010110000100000
# you can see that the number of times the game will be played
# is equal to the number of 0 at the end (till we reach the first 1)
# and then the number of 1 in front till this position
#
# this is visible if to understand that in binary the number is a
# perfect power if it has 1 and then all 0
def bits(n):
    s = bin(n)[2:]
    zerosAtEnd, onesAtFront, l = 0, 0, len(s)

    for i in xrange(l):
        if s[l - i - 1] == '0':
            zerosAtEnd += 1
        else:
            break

    for j in xrange(i, l):
        if s[l - j - 1] == '1':
            onesAtFront += 1

    return (zerosAtEnd + onesAtFront) % 2

print 'Richard' if bits(6) else 'Louise'
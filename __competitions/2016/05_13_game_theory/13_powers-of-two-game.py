# after investigation I found that you can divide all the numbers in +-i groups, where i
# is from 1 to 8. Apart from that only i = [1, 2, 4, 8] are possible
# second can win if the number of +- are the same. After some trial and error, I found that it
# happens if n % 8 == 0
for i in xrange(input()):
    if input() % 8:
        print 'First'
    else:
        print 'Second'
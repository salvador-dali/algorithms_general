def analysis(x, y):
    epsilon = 0.015
    zeros = [x[i] for i in xrange(len(x)) if -epsilon < y[i] < epsilon]
    ones_plus = [x[i] for i in xrange(len(x)) if -epsilon + 1 < y[i] < epsilon + 1]
    ones_minus= [x[i] for i in xrange(len(x)) if -epsilon - 1 < y[i] < epsilon - 1]

    if len(zeros):
        print 'sine-wave'
        period = (zeros[2] - zeros[1]) * 2
    else:
        print 'square-wave'
        period = abs(ones_plus[0] - ones_minus[0]) * 2

    frequency = 1.0 / period
    print int(round(frequency / 5)) * 5

x, y = [], []
for i in xrange(input()):
    a, b = map(float, raw_input().split())
    x.append(a)
    y.append(b)
    
analysis(x, y)
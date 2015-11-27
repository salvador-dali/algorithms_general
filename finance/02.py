def NPVCashInflows(start, inflows, rate):
    """ Calculates the Net Present Value of an investment of Start $, knowing
    that each next year it will bring Inflow[i] $ and the discount rate is Rate

    NPVCashInflows(100, [-90, 20, 190, -10, 40], 0.1)
    """
    value = -start
    r = 1 + rate

    for i in inflows:
        value += i / r
        r *= 1 + rate

    return value

def bondPriceChange(duration, oldInterest, newInterest):
    """ Approximate change of the price of the bond
    https://www.coursera.org/learn/understanding-financial-markets/lecture/AySWd/fixed-income-government-bonds-risks
    """
    return -duration * (newInterest - oldInterest) / (1 + oldInterest)

print bondPriceChange(6.55, 0.1, 0.12)
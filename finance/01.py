def profitabilityOfPercentageReturns(arr):
    res = 1
    for i in arr:
        res *= (1 + i / 100.)
    return res

def estimatedRate(full_rate, num_parts):
    """You have a full interest rate which should be paid in parts each number of times
    What is the total interest rate is it?

    example: The stated annual interest rate is 8%, but interest is compounded quarterly and he will
    make monthly payments. What is the EAR?
    """
    return (1 + full_rate / num_parts)**num_parts - 1

def futureValueRepeatedIncome(money, rate, num):
    """Saving Money per time interval, with time interval interest Rate, how much money
    will you have after Num times

    if x = 1 + rate, C = money, then this is a sum of \sum_{i=0}^{n-1} C * x^i which can
    be simplified with geometric progression

    Example:
    Gloria is 35 and trying to plan for retirement. She has put a budget together and plans to
    save $5,400 per year, starting at the end of this year, in a retirement fund until she is 58.
    Assume that she can make 5.0% on her account. How much will she have for retirement at age 58?

    Here money = 5400, rate = 0.05, year = 58 - 35
    """
    return money * (pow((1 + rate), num) - 1) / rate

def repeatedWithdrawal(money, rate, num):
    """
    If you are to withdraw Money each Num of years, with a Rate, how much money do you need:
    (((x - money) * rate) - money) * rate - money ... = 0, which is equal to
    x \cdot r^{n-1} = c \sum_{i=0}^{n-1}r^{i}

    Gerard has estimated that he is going to need enough in his retirement fund to withdraw $75,000
    per year beginning on his 66th birthday and for 19 additional years thereafter. How much will
    Gerard need in his retirement account at age 65 if his fund is expected to earn an annual
    return of 8.0%?
    """
    r = 1 + rate
    return money * (pow(r, num) - 1) / (r - 1) / pow(r, num)

def repeatedPayments(money, rate, num):
    """You took Money as a mortgage. You have to pay each Num years fixed amount of money with rate.
    What is this fixed amount?

    Example:
    The house costs $400,000. They have put a 10% down payment.
    You have fixed rate 15-year mortgage at a 7.75% APR with monthly payments.
    How much will be first monthly pay?

    rate = 0.0775
    money = 400000 * (1 - 0.1) * rate
    year = 15

    print repeatedPayments(money, rate, year) / 12
    """
    r = 1 + rate
    return money * pow(r, num - 1) * (r - 1) / (pow(r, num) - 1)

from math import ceil

# task 7
# money = 110000
# rate = 0.07
# res = 0
# for i in xrange(29, 29 + 20):
#     res += money * (1 + rate) ** i
#
# print res
# print repeatedPayments(res, rate, 28)

# task 8
# year = 5
# total = 11500
# rate1 = 0.07
# rate2 = 0.04
# x = repeatedPayments(total, rate1, year)
#
# a1 = total * (1 + rate1)**5
# a2 = x * (1+rate1) + x * (1 + rate1)**2
# borrow = (a1 - a2) / (1 + rate2)**3
# print borrow

# https://www.vanguard.co.uk/documents/portal/literature/investment-fundamentals-guide.pdf
# p 21
# print profitabilityOfPercentageReturns([-0.68, 20.38, 2.7, 19.6, 20.62, 30.92, -7.14, -13.69, -26.75, 21.08, 7.93, 24.55, 6.6, 10.3, -19.48, 20.56, 16.77, -6.17, 11.67, 21.15, 11.22])
# print profitabilityOfPercentageReturns([-2.41, 19.26, 8.59, 11.82, 12.57, 1.05, 9.93, 8.34, 10.71, 5.53, 8.04, 5.77, 3.30, 5.76, 7.59, 5.3, 4.82, 5.8, 5.93, 0.04, 7.92])
# print profitabilityOfPercentageReturns([6.68, 6.56, 6.55, 7.69, 6.26, 6.08, 5.9, 4.11, 4.02, 4.04, 4.89, 4.64, 5.32, 5.99, 2.77, 0.61, 0.76, 1.08, 0.52, 0.53, 0.56])
# print profitabilityOfPercentageReturns([-18.38, 20.58, 18.78, -3.86, -9.28, 12.40, 22.81, -1.26, -7.04, 26.52, 28.65, 28.99, 24.87, -8.52, -27.62, 23.09, 24.19, -5.12, 23, 2.45, 23.1])
print profitabilityOfPercentageReturns([-6.51, 25.97, 16.86, 28.68, 17.47, 20.59, -8.23, -14.09, -22.17, 17.89, 11.25, 20.78, 14.43, 7.36, -28.33, 27.33, 12.62, -2.18, 8.97, 18.66, 0.74])
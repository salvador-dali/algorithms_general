# https://www.interviewbit.com/problems/best-time-to-buy-and-sell-stocks-iii/
def stock3(A):
    max_profit = 0
    max_history_profit = {0:(0, (0,0))}
    min_day = 0
    for i in range(1,len(A)):
        if A[i] <= A[min_day]: min_day = i
        cur_diff = A[i]-A[min_day]
        if max_history_profit[i-1][0] > cur_diff:
            max_history_profit[i] = max_history_profit[i-1]
        else:
            max_history_profit[i] = (cur_diff, (min_day,i))

    max_future_profit = {len(A)-1:(0, (len(A)-1,len(A)-1))}
    max_day = len(A)-1
    for i in reversed(range(len(A)-1)):
        if A[i] > A[max_day]: max_day = i
        cur_diff = A[max_day] - A[i]
        if max_future_profit[i+1][0] > cur_diff:
            max_future_profit[i] = max_future_profit[i+1]
        else:
            max_future_profit[i] = (cur_diff, (i,max_day))
        if max_history_profit[i][0] + max_future_profit[i][0] > max_profit:
            max_profit = max_history_profit[i][0] + max_future_profit[i][0]
            max_split = i
    return max_profit
# https://www.interviewbit.com/problems/stepping-numbers/
def generate_stepping(min_v, max_v):
    prev, res = range(1, 10), []
    while prev:
        next = []
        for curr_num in prev:
            if min_v <= curr_num:
                res.append(curr_num)

            last_digit = curr_num % 10
            if last_digit == 0:
                next.append(curr_num * 10 + 1)
            elif last_digit == 9:
                next.append(curr_num * 10 + 8)
            else:
                next.append(curr_num * 10 + last_digit + 1)
                next.append(curr_num * 10 + last_digit - 1)

        prev = [el for el in next if el <= max_v]

    res.sort()
    if min_v == 0:
        return [0] + res

    return res


a = generate_stepping(1, 100)
print a
print [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 21, 23, 32, 34, 43, 45, 54, 56, 65, 67, 76, 78, 87, 89, 98]
# https://www.interviewbit.com/problems/largest-continuous-sequence-zero-sum/
from collections import defaultdict

def analyse(arr):
    h, s = defaultdict(list), 0
    h[0].append(0)
    for i in xrange(len(arr)):
        s += arr[i]
        h[s].append(i + 1)

    sequences, max_len = [], 0
    for i in h:
        if len(h[i]) > 1:
            attempt = h[i][-1] - h[i][0]
            if attempt > max_len:
                max_len = attempt
                sequences = [(h[i][0], h[i][-1])]
            elif attempt == max_len:
                sequences.append((h[i][0], h[i][-1]))

    sequences.sort()
    if len(sequences) == 0:
        return None

    return arr[sequences[0][0]:sequences[0][1]]

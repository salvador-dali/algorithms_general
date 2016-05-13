# https://www.interviewbit.com/problems/grid-unique-paths/
from math import factorial as f
def C(n, m):
    f(n + m) / f(m) / f(n)
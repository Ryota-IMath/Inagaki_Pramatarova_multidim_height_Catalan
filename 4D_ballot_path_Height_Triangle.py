from functools import lru_cache



def ht(t):
    return 3 * t[0] - t[1] - t[2] - t[3]

def altern(t, bd):
"""Retrurns the number of 4d ballot paths from (0,0,0, 0) to t = (n,n,n, n) with intermediate points 
x0, x1 and x2 and x3 such that each path does has a height function ht(t) which is
less than or equal to bd
"""
    count = 0
    if t == (0, 0, 0, 0):
        return 1
    if t[0] > 0 and t[0] - 1 >= t[1]:
        count += altern((t[0] - 1, t[1], t[2], t[3]), bd)
    if t[1] > 0 and t[1] - 1 >= t[2] and ht((t[0], t[1] - 1, t[2], t[3])) <= bd:
        count += altern((t[0], t[1] - 1, t[2], t[3]), bd)
    if t[2] > 0 and t[2] - 1 >= t[3] and ht((t[0], t[1], t[2] - 1, t[3])) <= bd:
        count += altern((t[0], t[1], t[2] - 1, t[3]), bd)
    if t[3] > 0 and ht((t[0], t[1], t[2], t[3] - 1)) <= bd:
        count += altern((t[0], t[1], t[2], t[3] -1), bd)
    return count

for i in range(6):
    s = ""
    for b in range(1, 3*i+1):
        s = s + " "+ str(b_paths((i, i, i, i), b))) + ","
    print(s)

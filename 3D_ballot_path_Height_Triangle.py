from functools import lru_cache



def ht(t):
    return 2 * t[0] - t[1] - t[2]

@lru_cache(None)
def b_paths(t, bd):
    """Retrurns the number of 3d ballot paths from (0,0,0) to t (n,n,n) with intermediate points 
x0, x1 and x2 such that each path does has a height function ht(t) which is
less than or equal to bd
"""
    if t == (0, 0, 0):
        return 1

    x0, x1, x2 = t
    count = 0

    if x0 > 0 and x0 - 1 >= x1:
        count += b_paths((x0 - 1, x1, x2), bd)

    if x1 > 0 and x1 - 1 >= x2 and ht((x0, x1 - 1, x2)) <= bd:
        count += b_paths((x0, x1 - 1, x2), bd)

    if x2 > 0 and ht((x0, x1, x2 - 1)) <= bd:
        count += b_paths((x0, x1, x2 - 1), bd)

    return count

for i in range(6):
    s = ""
    for b in range(1, 2*i+1):
        s = s + " "+ str(b_paths((i, i, i), b))) + ","
    print(s)

from functools import lru_cache


def ht(t):
    return 4 * t[0] - t[1] - t[2] - t[3] - t[4]

def ballot_paths(t, bd):
    count = 0
    if t == (0, 0, 0, 0, 0):
        return 1
    if t[0] > 0 and t[0] - 1 >= t[1]:
        count += ballot_paths((t[0] - 1, t[1], t[2], t[3], t[4]), bd)
    if t[1] > 0 and t[1] - 1 >= t[2] and ht((t[0], t[1] - 1, t[2], t[3], t[4])) <= bd:
        count += ballot_paths((t[0], t[1] - 1, t[2], t[3], t[4]), bd)
    if t[2] > 0 and t[2] - 1 >= t[3] and ht((t[0], t[1], t[2] - 1, t[3], t[4])) <= bd:
        count += ballot_paths((t[0], t[1], t[2] - 1, t[3], t[4]), bd)
    if t[3] > 0 and t[3]-1>=t[4] and ht((t[0], t[1], t[2], t[3] - 1, t[4])) <= bd:
        count += ballot_paths((t[0], t[1], t[2], t[3] -1, t[4]), bd)
    if t[4] > 0 and ht((t[0], t[1], t[2], t[3], t[4]-1)) <= bd:
        count += ballot_paths((t[0], t[1], t[2], t[3], t[4] -1), bd)
    return count

for i in range(10):
    s = ""
    for b in range(1, 4*i+1):
        s = s + str(ballot_paths((i, i, i, i, i), b)) + ", "
    print(s)
    

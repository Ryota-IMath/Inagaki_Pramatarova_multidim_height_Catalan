
from functools import lru_cache

n = 6 # length - 3n
s = 6 # number of peaks - s


"""
    Counts the number of 4D ballot paths of length 4n
    that contain exactly s peaks.
    
    A peak is defined as one of the substrings 'xy', 'xz', or 'xw',
    where the first step is 'x' and the next step is either 'y', 'z', or 'w'.
    
    Parameters:
      x_rem, y_rem, z_rem, w_rem : remaining steps of each type
      x_used, y_used, z_used, w_used : steps used so far
      last_char : 0 for 'x', 1 for 'y', 2 for 'z', 3 for 'w', -1 if none yet
      s_needed : number of peaks still required
"""

def count_dyck_words(x_rem, y_rem, z_rem, w_rem, x_used, y_used, z_used, w_used, last_char, s_needed):
    if x_rem == y_rem == z_rem == w_rem == 0:
        return 1 if s_needed == 0 else 0
    if not (x_used >= y_used >= z_used >= w_used):
        return 0
    if s_needed < 0:
        return 0
    total = 0
    if x_rem > 0:
        total += count_dyck_words(x_rem - 1, y_rem, z_rem, w_rem,
                                  x_used + 1, y_used, z_used, w_used,
                                  0, s_needed)
    if y_rem > 0 and x_used >= y_used + 1:
        used = 1 if last_char == 0 else 0  
        total += count_dyck_words(x_rem, y_rem - 1, z_rem, w_rem,
                                  x_used, y_used + 1, z_used, w_used,
                                  1, s_needed - used)
    if z_rem > 0 and y_used >= z_used + 1:
        used = 1 if last_char == 0 else 0  
        total += count_dyck_words(x_rem, y_rem, z_rem - 1, w_rem,
                                  x_used, y_used, z_used + 1, w_used,
                                  2, s_needed - used)
    if w_rem > 0 and z_used >= w_used + 1:
        used = 1 if last_char == 0 else 0  
        total += count_dyck_words(x_rem, y_rem, z_rem, w_rem - 1,
                                  x_used, y_used, z_used, w_used + 1,
                                  3, s_needed - used)
    return total
def main():
    result = count_dyck_words(n, n, n, n, 0, 0, 0, 0, -1, s)
    print(f"Number of 4d Narayana paths n={n}, s={s} → {result}")
if __name__ == "__main__":
    main()

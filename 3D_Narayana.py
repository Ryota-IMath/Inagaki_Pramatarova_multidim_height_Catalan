from functools import lru_cache
n = 6 # length - 3n
s = 6 # number of peaks - s
@lru_cache(None)
def count_paths_with_s_peaks(x_rem, y_rem, z_rem, x_used, y_used, z_used, last_char, s_needed):
    """
    Returns the number of 3d ballot paths using exactly x_rem 'x's, y_rem 'y's, and z_rem 'z's
    such that exactly needed_s substrings of type 'xy' or 'xz' remain to form (as defined as peaks),
    given that the previous character placed was last_char:
      last_char = 0 for 'x', 1 for 'y', 2 for 'z', or -1 if none yet.
    """
    if x_rem == 0 and y_rem == 0 and z_rem == 0:
        return 1 if s_needed == 0 else 0
    if not (x_used >= y_used >= z_used):
        return 0
    if s_needed < 0:
        return 0

    total = 0
    if x_rem > 0:
        total += count_paths_with_s_peaks(x_rem - 1, y_rem, z_rem,
                                  x_used + 1, y_used, z_used,
                                  0, s_needed)
    if y_rem > 0 and x_used >= y_used + 1:
        used = 1 if last_char == 0 else 0
        total += count_paths_with_s_peaks(x_rem, y_rem - 1, z_rem,
                                  x_used, y_used + 1, z_used,
                                  1, s_needed - used)
    if z_rem > 0 and y_used >= z_used + 1:
        used = 1 if last_char == 0 else 0
        total += count_paths_with_s_peaks(x_rem, y_rem, z_rem - 1,
                                  x_used, y_used, z_used + 1,
                                  2, s_needed - used)
    return total
def main():
    result = count_paths_with_s_peaks(n, n, n, 0, 0, 0, -1, s)
    print(f"Number of 3d Narayana paths for ={n}, s={s} → {result}")
if __name__ == "__main__":
    main()

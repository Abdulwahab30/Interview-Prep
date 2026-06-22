def iso(s, t):
    if len(s) != len(t):
        return False

    map_st = {}
    map_ts = {}

    for i in range(len(s)):
        c1 = s[i]
        c2 = t[i]

        # 1. Check existing mapping from s -> t
        if c1 in map_st:
            if map_st[c1] != c2:
                return False  # c1 tries to map to a new/different character
        else:
            map_st[c1] = c2

        # 2. Check existing mapping from t -> s
        if c2 in map_ts:
            if map_ts[c2] != c1:
                return False  # c2 tries to map back to a different character
        else:
            map_ts[c2] = c1

    return True


# Testing the function
print(iso("egg", "add"))  # Expected: True (e->a, g->d)
print(iso("egg", "ada"))  # Expected: False (g tries to map to both d and a)
print(iso("abc", "aaa"))  # Expected: False (b and c both try to map to a)
def wordPattern(a,b):
    map_ab = {}
    map_ba = {}
    d=b.split()
    
    if len(a) != len(d):
            return False

    for i in range(len(a)):
        c1 = a[i]
        c2 = d[i]
    
        # 1. Check existing mapping from s -> t
        if c1 in map_ab:
            if map_ab[c1] != c2:
                return print("False")  # c1 tries to map to a new/different character
        else:
            map_ab[c1] = c2
        
        # 2. Check existing mapping from t -> s
        if c2 in map_ba:
            if map_ba[c2] != c1:
                return False  # c2 tries to map back to a different character
        else:
            map_ba[c2] = c1

    return print("True")

wordPattern("abba","dog cat cat dog")
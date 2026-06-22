def is_anagram(s, t):
    s_map={}
    t_map={}

    for i in s:
        if i in s_map:
            s_map[i]+=1
        else:
            s_map[i] =1
    for i in t:
        if i in t_map:
            t_map[i]+=1
        else:
            t_map[i] =1
    if s_map == t_map:
        print("True")
    else:
        print("False")

is_anagram("listen","listte")
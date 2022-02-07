def remove(s):
    if(s[len(s)-1:] == '!'): return s[:-1]
    return s

def abbrev_name(name):
    arr = name.split(" ")
    s = ""
    for word in arr:
        s += word[:1] + "."

    return s[:-1].upper()

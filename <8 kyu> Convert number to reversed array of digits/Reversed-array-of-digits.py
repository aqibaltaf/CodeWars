def digitize(n):
    arr = []
    if n == 0: return [0]
    while(n>0):
        r = n % 10
        arr.append(r)
        n = n // 10

    return arr

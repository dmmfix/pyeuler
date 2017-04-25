def zero(t):
    zt = []
    for r in range(0, len(t)):
        zt.append([0] * len(t[r]))
    return zt

def max_path(t, lens, r, c):
    if (lens[r][c] == 0):
        if (r == len(t)-1):
            lens[r][c] = t[r][c]
        else:
            lens[r][c] = t[r][c] + max_path(t, lens, r+1,c)
            if (c+1 < len(t[r+1])):
                lens[r][c] = max(t[r][c] + max_path(t, lens, r+1,c+1), lens[r][c])
    return lens[r][c]

def read(fname):
    t = []
    for l in open(fname):
        t.append(map(int, l.split()))
    return t



def center_of(a): 
    if len(a) % 2 != 0: 
        b = len(a) // 2
        return a[b]
    else: 
        d = len(a) // 2
        return (a[d-1] + a[d])
def print_in_box(a): 
    b = len(a) * '-'
    c = len(a) * ' '
    print(f" +-{b}-+ ")
    print(f" | {c} | ")
    print(f" | {a} | ")
    print(f" | {c} | ")
    print(f" +-{b}-+ ")


    def print_in_box(a): 
    b = len(a) * '-'
    c = len(a) * ' '
    d = ' ' * 4         
    print(f" +-{b}-+ ")
    print(f" | {c} | ")
    print(f" | {a[0:len(a)-4]}{d} | ")
    print(f" | {c} | ")
    print(f" +-{b}-+ ")
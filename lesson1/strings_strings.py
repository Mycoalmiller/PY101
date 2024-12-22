b = []
def function(a):
    if a % 2 == 0: 
        b.append(('10' * (a//2)))
    if a % 2 != 0: 
        b.append (('10' * (a//2)) + '1')
    c = b[0]
    return c 

print(function(8))
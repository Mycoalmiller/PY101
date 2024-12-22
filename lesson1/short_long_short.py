
def short_long_short(a,b): 
    if len(a) > len(b): 
        c = b + a + b
        return c
    elif len(a) < len(b): 
        c = a + b + a
        return c

print(short_long_short('abc', 'defgh'))
print(short_long_short('abcde', 'fgh')) 
print(short_long_short('', 'xyz'))
a = str(input('what is your name?'))

def name(a):
    if not '!' in a: 
        return (f'what is your name? {a}' 
                f' Hello {a}.  ')
    else: 
        return  (f'what is your name? {a}'
                 f' Hello {a.upper()}. WHY ARE WE YELLING?')

print(name(a))
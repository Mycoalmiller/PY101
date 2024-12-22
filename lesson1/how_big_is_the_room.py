a = input('do you prefer feet or meters')

def meters_or_feet(a): 
    if a == 'meters' or 'feet':
        return True 
    else: 
        Print('please enter feet or meters')

if True: 
    a = int(input('what is the width of your room, in feet'))
    b = int(input('what is the length of your room, in feet'))

def area_of_room(a,b):
    ft = a * b 
    mt = (a * b) / 10.7639
    print(f'The area of your room is {ft} feet and {mt} meters')

area_of_room(w,l)
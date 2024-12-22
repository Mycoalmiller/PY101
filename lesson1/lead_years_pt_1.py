
def is_leap_year(a): 
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):
        return True
    elif (a % 100 == 0 and a % 400 != 0):
        return False
    else: 
        return False
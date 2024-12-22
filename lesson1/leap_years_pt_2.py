def is_leap_year(a):
    if a <= 1751:  
        if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0): 
            return True
        elif (a % 100 == 0 and a % 400 != 0):
            return False
        else: 
            return False
    if a >= 1752:
        if (a % 4 == 0):
            return True
        else: 
            return False
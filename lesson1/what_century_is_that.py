first = 'st'
second = 'nd'
third = 'rd'
fourth = 'th'

def century(year): 
    number = round(year//100) + 1
    number_str = str(number)
    if number >= 10 and number <= 20: 
        return number_str +  fourth
    elif number_str[len(number_str)-1] == '1':
        return number_str + first
    elif number_str[len(number_str)-1] == '2':
        return number_str + second
    elif number_str[len(number_str)-1] == '3':
        return number_str + third                
    else: 
        return number_str + fourth 
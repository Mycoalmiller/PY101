





def function(string, letter): 
    count = 0
    for index, string_letter in enumerate(string): 
        if string_letter == letter: 
            count += 1
            if count == 3: 
                return index
    return -1


print(function('xyzxyzxyz', 'x'))
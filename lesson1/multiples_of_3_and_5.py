list = []
def multisum(a): 
    for a in range(a+1): 
        if (a % 3 == 0) or (a % 5 == 0): 
            list.append(a)

multisum(1000)
print(sum(list))
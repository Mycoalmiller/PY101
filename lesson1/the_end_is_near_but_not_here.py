def penultimate(a): 
    b = a.split(" ")
    return b[len(b)-2]

    

a = input('phrase:')
for b in a:
    if a != type(str): 
        break

def edge_case(a):
    b = a.split(" ")
    print (b[len(b) // 2])

edge_case(a)
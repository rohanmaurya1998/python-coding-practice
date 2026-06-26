def greatest(a,b):
    if a>b:
        return 'a is greatest',a
    elif a==b:
        return 'both are equal',(a,b)
    return 'b is greatest',b
print(greatest(23,55))
print(greatest(23,23))
print(greatest(45,2))

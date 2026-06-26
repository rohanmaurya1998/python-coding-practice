def check(n):
    if n>0:
        return 'positive',n
    elif n==0:
        return 'zero number',n
    elif n<0 and n!=0:
        return 'negative number',n
print(check(45))
print(check(0))
print(check(-34))
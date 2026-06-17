#wap to find the largest number from the given numbers 
a=eval(input('enter the number a '))
b=eval(input('enter the number b '))
c=eval(input('enter the number c '))
if a<b:
    if a<c:
        print('a is smallest  number ')
elif b<c:
    if b<a:
        print('b is the smallest  number ')
elif c<a:
    if c<b:
        print('c is the smallest  number ')
else:
    print('enter a valid input ')
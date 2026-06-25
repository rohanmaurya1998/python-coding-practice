# wap to print the half pyramid without space 
n=int(input('enter the number '))
for i in range(n):
    for j in range(i+1):
        print('*',end='')
    for k in range(n-i-1):
        print('',end='')
    print()
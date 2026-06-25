# wap to print the full pyramid 
n=int(input('enter the number of rows'))
for i in range(n):
    for j in range(n-i-1):# for printing the space 
        print(' ',end='')
    for k in range(2*i+1):# for printing the stars
        print('*',end='')
    print()
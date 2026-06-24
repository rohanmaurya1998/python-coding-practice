# wap to print the left * triangle 
n=int(input('enter the number of rows '))
for i in range(n):
    for j in range(i+1):# start incresing in the each row
        print('*', end='')
    print()
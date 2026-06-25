# wap to print the inverted left triangle
n=int(input('enter the number of rows'))
for i in range(n):
    for j in range(n-i):
        print('*',end='')
    print()
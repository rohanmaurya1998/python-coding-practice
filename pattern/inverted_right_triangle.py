# wap to print the inverted right triangle
n=int(input('enter the number of rows'))
for i in range(n):
    for j in range(i):# for printing the spaces
        print(' ',end='')
    for k in range(n-i):# for printing *
        print('*',end='')
    print()

    # remember one thing if you ever confuse in this codes then dry run this 
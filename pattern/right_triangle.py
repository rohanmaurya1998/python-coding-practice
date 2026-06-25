# wap to print the right * triangle 
n=int(input('enter the number '))
for i in range(n):
    for j in range(n-i-1): # print spaces 
        print('',end='')
    for k in range(i+1): # print *
            print('*',end='')
    print()
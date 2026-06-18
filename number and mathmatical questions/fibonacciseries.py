#wap to print the fibonacci series 
n=int(input('enter the number of iteration '))
a=0
b=1
for i in range(1,n+1):
    print(a,end=' ')
    a,b=b,a+b
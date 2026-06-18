#wap to print the all the factor of a number 
n=int(input('enter the number '))
factor=[]
for i in range(1,n+1):
        if n%i==0:
            factor.append(i)
print(factor)
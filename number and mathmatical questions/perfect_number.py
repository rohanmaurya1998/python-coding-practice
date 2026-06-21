#wap to print the perfect number 
''' what is perfect number 
perfect number= sum of its proper factors except number itself = number itself 
6=factor of 6
            =1,2,3,6(except 6)
            sum of factors=1+2+3=6
            sp 6 is the perfect number 
            '''

n=int(input('enter the number '))
factor_sum=0
factors=[]
for i in range(1,n):
    if n%i==0:
        factors.append(i)
for i in factors:
    factor_sum+=i
if factor_sum==n:
    print('perfect number ')
else:
    print('not a perfect number ')
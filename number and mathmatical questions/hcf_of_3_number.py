#wap to print the hcf of n numbers
n1=int(input('enter the number '))
n2=int(input('enter the number '))
n3=int(input('enter the number '))
smaller=min(n1,n2,n3)
for i in range(1,smaller+1):
    if n1%i==0 and n2%i==0 and n3%i==0:
        hcf=i
print(hcf)


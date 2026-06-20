#wap to print the hcm of two number 
n1=int(input('enter the number 1\n'))
n2=int(input('enter the number 1\n'))
lcm=0
bigger=max(n1,n2)
while True:
    if bigger%n1==0 and bigger%n2==0:
        lcm=bigger
        break
    bigger+=1
print(lcm)

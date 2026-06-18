#wap to print the sum of all odd digits
n=int(input('enter the number '))
sum=0
while n>0:
    for i in range(len(str(n))):
        digit=n%10
        if digit%2!=0:
            sum+=digit
        n=n//10
print(sum)
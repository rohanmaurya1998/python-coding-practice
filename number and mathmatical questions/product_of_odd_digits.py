#wap to product of  the odd digits from a given number 
#wap to print the product of even digits
n=int(input('enter the number '))
product=1
while n>0:
    for i in range(len(str(n))):
        digit=n%10
        if digit%2!=0:
            product*=digit
        n=n//10
print(product)
#wap to print the reverse the number 
n=int(input('enter the number '))
rev=0
while n>0:
    for i in range(len(str(n))):
        digit=n%10
        rev=rev*10+digit
        n=n//10
print('reversed number is:\n',rev)
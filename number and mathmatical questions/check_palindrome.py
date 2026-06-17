#wap to check the  number is palindrome or not 
n=int(input('enter the number '))
original=n
rev=0
while n>0:
    for i in range(len(str(n))):
        digit=n%10
        rev=rev*10+digit
        n=n//10
if original==rev:
    print('palindrome')
else:
    print('not a palindrome')
    
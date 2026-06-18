# wap to check the number is prime or not 
n=int(input('enter the number '))
if n<=1:
    print('not prime')
for i in range(2,n):
    if n%i==0:
      print('not prime')
      break
    
else:
    print('prime')
#wap to check the number is a strong number or not 
''' strong number=>
                  sum of factorial of each digits
                  145=1!+4!+5!
                      =1+24+120
                      =145

                
                
                '''

n=int(input('enter the number '))
og=n
total=0
while n>0:
    digit=n%10
    fact=1
    for i in range(1,digit+1):
        
        fact*=i
    total+=fact
    n=n//10
if total==og:
    print('strong number ')
else:
    print('not a strong number ')
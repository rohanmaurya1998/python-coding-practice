# wap to check the given number is armstrog number or not 
'''
armstrong number =>
                   sum of all the digits in the number having power  the count of the digit on each digit 
                   153= 1*3+5*3+3*3
                       1+125+27=153

'''
n=int(input('enter the number '))
count=0
digit_sum=0
og=n
for i in range(len(str(n))):
    n=n//10
    count+=1
power=count
for i in str(og):
    digit_sum+=int(i)**power
if digit_sum==og:
    print('armstrong number ')
else:
    print('not a armstrong number ')


#wap to count the odd digits from a given number 
n=int(input('enter the number '))
count=0
while n>0:
    for i in range(len(str(n))):
        digit=n%10
        if digit%2!=0:
            count+=1
        n=n//10
print(count)
# wap to convert the number into binary to decimal
n=int(input('enter the number '))
binary=""
while n>0:
    rem=n%2
    binary=str(rem)+binary # here we use concatination logic we conert rem into string and merge it with binary
    n=n//2
print(binary)


#another logic using list and string 
decimal=int(input('enter the number '))
list=[]
while decimal>0:
    rem=decimal%2
    list.append(rem)
    decimal=decimal//2

list.reverse()
for i in list:
    print(i,end=' ')
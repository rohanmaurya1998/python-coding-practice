# to get the binary to decimal we have to multiply the each digit with the power of two and then add them
#method 1 -- using the loop
binary=(input('enter the number '))
decimal=0
power=0
for i in binary[::-1]:
    decimal=decimal+int(i)*(2**power)# 0+1*(2*0)=0+1*1=1(for first iteration)
    power+=1
print(decimal)
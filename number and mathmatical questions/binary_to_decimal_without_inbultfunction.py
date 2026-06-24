#wap to convert the binary to decimal without using the inbult function
binary=input('enter the binary number ')
decimal=0
for i in binary:
    decimal=decimal*2+int(i)
print(decimal)


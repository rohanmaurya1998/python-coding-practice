#find the power of a number without using the **
base=int(input('enter the number' ))
power=int(input('enter the power'))
result=1
for i in range(power):
    result=result*base
print(result)
'''
Dry run-- for base 3 power 3
      for the first iteration result=1 so, res*base=1*3=3
      2nd iteration res*base=3*3=9
      3rd iteration res*base 9*3=27


'''
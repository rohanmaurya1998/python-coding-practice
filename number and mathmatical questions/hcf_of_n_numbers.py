#wap to print the hcf of n numbers
nums=list(map(int,input('enter numbers\n').split()))
smaller=min(nums)
hcf=1
for i in range(1,smaller+1):
    common =True
    for num in nums:
        if num%i !=0:
            common=False
            break
    if common:
        hcf=i
print(hcf)
#wap to build a basic calculator 
n1=eval(input('enter the number '))
n2=eval(input('enter the umber '))
opr=input('enter the operator ')
if opr=='+':
    print('sum is : ',n1+n2)
elif opr=='-':
    print('subtraction is : ',n1-n2)
elif opr=='*':
    print('product is :',n1*n2)
elif opr=='/':
    print('division is :',n1/n2)
else:
    print('enter a valid input ')
# wap to print the ractangle pattern  where row=3, column=5
row=3
column=5
# n=int(input('enter the number of rows'))
for i in range(row):
    for j in range(column):
        print('*',end='')
    print()
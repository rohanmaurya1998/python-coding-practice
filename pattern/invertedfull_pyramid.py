#wap to print the inverted full pyramid 
n = int(input("Enter the number of rows: "))

for i in range(n):
    # Print leading spaces
    for j in range(i):
        print(" ", end="")

    # Print stars
    for k in range(2 * (n - i) - 1):
        print("*", end="")

    print()
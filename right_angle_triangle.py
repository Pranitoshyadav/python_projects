print("halp piramid patern")

n = int(input("enter the row : "))

for i in range(n):
    for j in range(i + 1):
        print("*", end = " ")
    print()
def add(P, Q):
    return P+Q

def substract(P, Q):
    return P-Q

def multiply(P, Q):
    return P*Q

def divide(P, Q):
    return P/Q

print("choose a oppration : ")
print("a. add")
print("b. substract")
print("c. multiply")
print("d. divide")

choice = input("enter a choice (a/b/c/d) : ")
num_1 = int(input("enter the frist num : "))
num_2 = int(input("enter the second num : "))

if choice == "a":
    print(num_1, " + ", num_2, " = ", add(num_1, num_2))

if choice == "b":
    print(num_1, " - ", num_2, " = ", substract(num_1, num_2))

if choice == "c":
    print(num_1, " * ", num_2, " = ", multiply(num_1, num_2))

if choice == "d":
    print(num_1, " / ", num_2, " = ", divide(num_1, num_2))

else :
    print("this is an invalid input")
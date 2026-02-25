"""Take an input for buing and selling cost and then figure out if it was profit / loss/ neither """

a = int(input("Enter the buying price : "))
b = int(input("Enter the selling price : "))

if b > a :
    profit = b-a
    print(f"Profit : {profit}")
    
elif a > b :
    loss = a-b
    print(f"Loss : {loss}")
    
else:
    print("Neither profit nor loss")
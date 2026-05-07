try: 
    number = int(input("Enter a number : "))
    print("the number is entered as ",number)
except ValueError as ex:
    print("exception ",ex)


try:
    num1 ,num2 = eval(input("Enter two numbers seperated by commas : "))
    result = num1 / num2
    print("Result is ",result)
except ZeroDivisionError:
    print("Devided by zero is error")
except SyntaxError:''
    print("Comma is missing please enter like this : 1, 2")
except:
    print("Wrong Output")
else:
    print("No exceptions")
finally:
    print("This will print no matter what")


valid = False
while not valid:
    try:
        n = int(input("Enter a number : "))
        while n % 2 == 0:
            print("bye")
            valid = True
    except ValueError
        print("invalid")
# 1) Ask the user to enter the number of electricity units consumed and store it in `units`.

# 2) Use if–elif–else to decide the cost based on `units`:

# - If `units` is less than 50:

# Set `amount` as units × 2.60 and set `surcharge` as 25.

# - Else if `units` is 100 or less:

# Set `amount` as (cost for first 50 units) + (remaining units × 3.25)

# Set `surcharge` as 35.

# - Else if `units` is 200 or less:

# Set `amount` as (cost for first 50 units) + (cost for next 50 units) + (remaining units × 5.26)

# Set `surcharge` as 45.

# - Else (units more than 200):

# Set `amount` as (cost for first 50) + (next 50) + (next 100) + (remaining units × 8.45)

# Set `surcharge` as 75.

# 3) Calculate the final bill:

# total = amount + surcharge

# 4) Print the electricity bill (`total`) in 2 decimal places

units = int(input("enter a the electricity usege : "))

if units < 50 :
    ammount = units * 2.6
    surchange = 25
elif units <= 100 :
    ammount = 130 + ((units - 50) * 3.25)
    surchange = 35
elif units <= 200 :
    ammount = 130 + 162.50 + ((units - 100) * 5.26)
else :
    ammount = 130 + 162.50 + 526 + ((units - 200) * 8.45)
    surchange = 75

total = ammount + surchange

print(total)
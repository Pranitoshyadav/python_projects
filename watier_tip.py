def total_calc(bill_ammount, tip_per):
    total = bill_ammount * (1 + 0.01 * tip_per)
    tatal = round(total, 2)
    print(f"please pay ${total}")

total_calc(150, 20)
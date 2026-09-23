name = input("Enter Customer Name: ")
units = float(input("Enter Units Consumed: "))

if units < 0:
    print("Invalid input! Units consumed cannot be negative.")
else:
    # slab calculation
    if units <= 100:
        charge = units * 1.50
    elif units <= 200:
        charge = (100 * 1.50) + ((units - 100) * 2.50)
    elif units <= 500:
        charge = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
    else:
        charge = (100 * 1.50) + (100 * 2.50) + (300 * 4.00) + ((units - 500) * 6.50)

    tax = charge * 0.05
    total_bill = charge + tax

    print("\n--- Electricity Bill ---")
    print(f"Customer Name  : {name}")
    print(f"Units Consumed : {units:.1f}")
    print(f"Energy Charge  : Rs. {charge:.2f}")
    print(f"Tax (5%)       : Rs. {tax:.2f}")
    print(f"Total Bill     : Rs. {total_bill:.2f}")

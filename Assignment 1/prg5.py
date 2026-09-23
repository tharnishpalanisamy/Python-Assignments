num_products = int(input("Enter number of products: "))
prices = []

for i in range(num_products):
    while True:
        p = float(input(f"Enter price for product {i + 1}: "))
        if p >= 0:
            prices.append(p)
            break
        print("Price cannot be negative. Try again.")

subtotal = sum(prices)

# discount based on subtotal
if subtotal >= 5000:
    discount_percent = 20
elif subtotal >= 2500:
    discount_percent = 10
elif subtotal >= 1000:
    discount_percent = 5
else:
    discount_percent = 0

discount = (subtotal * discount_percent) / 100
amount_after_discount = subtotal - discount
tax = amount_after_discount * 0.05
final_amount = amount_after_discount + tax

print("\n--- Shopping Bill Summary ---")
print(f"Number of Items : {num_products}")
print(f"Subtotal        : Rs. {subtotal:.2f}")
print(f"Discount ({discount_percent}%)   : Rs. {discount:.2f}")
print(f"Tax (5%)        : Rs. {tax:.2f}")
print(f"Final Amount    : Rs. {final_amount:.2f}")

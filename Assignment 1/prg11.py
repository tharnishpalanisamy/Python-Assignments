accounts = {
    "1001": {
        "name": "Tharnish",
        "balance": 5000.0,
        "history": ["Account opened with Rs. 5000.00"]
    }
}

while True:
    print("\n===== MINI BANKING APPLICATION =====")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Transaction History")
    print("6. Exit")

    choice = input("Enter choice (1-6): ")

    match choice:
        case "1":
            acc_no = input("Enter new Account Number: ").strip()
            if acc_no in accounts:
                print("Account number already exists!")
                continue

            name = input("Enter Account Holder Name: ").strip()
            initial_dep = float(input("Enter Initial Deposit: "))

            if initial_dep < 500:
                print("Minimum initial deposit is Rs. 500.")
            else:
                accounts[acc_no] = {
                    "name": name,
                    "balance": initial_dep,
                    "history": [f"Account opened with Rs. {initial_dep:.2f}"]
                }
                print(f"Account created successfully for {name} (Acc No: {acc_no}).")

        case "2":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no not in accounts:
                print("Account not found.")
                continue

            amt = float(input("Enter deposit amount: "))
            if amt <= 0:
                print("Deposit amount must be positive.")
            else:
                accounts[acc_no]["balance"] += amt
                accounts[acc_no]["history"].append(f"Deposited: Rs. {amt:.2f}")
                print(f"Successfully deposited Rs. {amt:.2f}.")
                print(f"Current Balance: Rs. {accounts[acc_no]['balance']:.2f}")

        case "3":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no not in accounts:
                print("Account not found.")
                continue

            amt = float(input("Enter withdrawal amount: "))
            if amt <= 0:
                print("Amount must be positive.")
            elif amt > accounts[acc_no]["balance"]:
                print("Insufficient balance!")
            else:
                accounts[acc_no]["balance"] -= amt
                accounts[acc_no]["history"].append(f"Withdrawn: Rs. {amt:.2f}")
                print(f"Please collect cash: Rs. {amt:.2f}")
                print(f"Remaining Balance: Rs. {accounts[acc_no]['balance']:.2f}")

        case "4":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                acc = accounts[acc_no]
                print(f"\nHolder Name : {acc['name']}")
                print(f"Balance     : Rs. {acc['balance']:.2f}")
            else:
                print("Account not found.")

        case "5":
            acc_no = input("Enter Account Number: ").strip()
            if acc_no in accounts:
                print(f"\nTransaction History for {accounts[acc_no]['name']}:")
                for item in accounts[acc_no]["history"]:
                    print(f" - {item}")
            else:
                print("Account not found.")

        case "6":
            print("Thank you for banking with us!")
            break

        case _:
            print("Invalid choice, please select between 1 and 6.")

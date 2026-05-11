print("Budget Tracker Program\n")
bills = []
total_spent = 0
expenses = [
      'Savings',
      'Food',
      'Electricity',
      'Water',
      'Transportation Expenses',
      'Essential Clothing'
      ]
budget = int(input("\nEnter budget: "))
real_budget = budget

while True:
    

    print("\n----Payments----")
    for index, item in enumerate(expenses):
        print(f"|{index + 1}| {item}")
        
    choice = int(input("\nChoose a number: "))
    
    if choice in [1,2,3,4,5,6]:
        bill_amount = float(input(f"""-Paying {expenses[choice - 1]}
Please enter amount: """))
        bills.append((expenses[choice - 1], bill_amount))
        real_budget -= bill_amount
        total_spent += bill_amount
        print(f"\nBudget remaining: {real_budget}")
        
        if real_budget < bill_amount:
            print("Insufficient balance")
            break
        
        conti = input("Do you want to continue (y/n): ").lower()
        if conti == 'y':
            continue
        if conti == 'n':
            break
    elif choice == 0:
        ("Finishing...\n")
    else:
        print("Invalid choice. Try again!")
        continue

print(f"""\n=====================
     TOTAL BILL
=====================\n""")    

for name, amount in bills:
    print (f"{name:}: {amount: .2f}")
print(f"Total Spent: {total_spent:.2f}")
print(f"Remaining:   {real_budget:.2f}")

print("""\n=====================
Thank you, exiting...""")

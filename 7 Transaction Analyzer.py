def print_transactions(transactions):
  for transaction in transactions:
    amount = transaction[0]
    statement = transaction[1]
    print(f"${amount} - {statement}")


def print_summary(transactions):
  deposits = [transaction[0] for transaction in transactions if transaction[0] > 0]
  total_deposits = sum(deposits)
  print(f"\nTotal deposited: ${total_deposits}")

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawn = sum(withdrawals)
  print(f"Total withdrawn: ${total_withdrawn}")

  balance = total_deposits + total_withdrawn
  print(f"Balance: ${balance}")


def analyze_transactions(transactions):
  transactions.sort()
  deposits = [transaction[0] for transaction in transactions if transaction[0] > 0]
  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  largest_withdrawal = min(withdrawals)
  largest_deposit = max(deposits)
  print("\nLargest withdrawal: $",largest_withdrawal, "\nLargest deposit: $",largest_deposit)

  deposits = [transaction[0] for transaction in transactions if transaction[0] > 0]
  total_deposit = sum(deposits)
  if len(deposits) > 0:
    average_deposit = total_deposit/len(deposits)
  elif len(deposits) == 0:
    average_deposit = 0
  print("Average deposit: $",average_deposit)

  withdrawals = [transaction[0] for transaction in transactions if transaction[0] < 0]
  total_withdrawals = sum(withdrawals)
  if len(withdrawals) > 0:
    average_withdrawals = total_withdrawals/len(withdrawals)
  elif len(withdrawals) == 0:
    average_withdrawals = 0
  print("Average withdrawals: $",average_withdrawals)

def add_transaction(transactions):
    try:
        amount = float(input("Enter transaction amount (negative for withdrawal): "))
        statement = input("Enter transaction description: ")
        transactions.append((amount, statement))
        print("Transaction added successfully!")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

data = [
  (749.17, "Investment Return"),
  (-11.54, "Utilities"),
  (-247.58, "Online Shopping"),
  (981.17, "Investment Return"),
  (-410.65, "Rent"),
  (310.60, "Rent"),
  (563.70, "Gift"),
  (220.79, "Salary"),
  (-49.85, "Car Maintenance"),
  (308.49, "Salary"),
  (-205.55, "Car Maintenance"),
  (870.64, "Salary"),
  (-881.51, "Utilities"),
  (518.14, "Salary"),
  (-264.66, "Groceries")
]

print("Welcome to the transaction analyzer.")

while True:
  print("\nOptions:")
  print("1 - View Balance")
  print("2 - View Recent Transactions")
  print("3 - View Average Deposit & Withdrawal Amounts")
  print("4 - Add Transaction/s")
  print("5 - Close Program")
  choice = input("Enter your choice: ")
  if choice == "1":
    print_summary(data)
  elif choice == "2":
    print()
    print_transactions(data)
  elif choice == "3":
    analyze_transactions(data)
  elif choice == "4":
    add_transaction(data)
  elif choice == "5":
    break
  else:
    print("Invalid choice")
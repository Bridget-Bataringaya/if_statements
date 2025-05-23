# ATM Withdrawal Program

# Sample account balance
account_balance = 5000.00

# Ask user for withdrawal amount
withdrawal_amount = float(input("Enter the amount you want to withdraw: "))

# Check if sufficient balance is available
if withdrawal_amount <= account_balance:
    account_balance -= withdrawal_amount
    print(f"Withdrawal successful! Your new balance is: ${account_balance:.2f}")
else:
    print("Insufficient balance. Withdrawal denied.")

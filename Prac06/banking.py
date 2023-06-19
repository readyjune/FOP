from accounts import BankAccount

account = BankAccount('Everyday','007',3000)

print("Welcome to my bank")

print("Hello", account.name, "\tNuber: ", account.number, "\tBalance: ", account.balance)

choice = input('Enter transaction selection: (W)withdrawl, (D)eposit, (I)nterest, (B)alance, e(X)it...')

choice = choice.upper()

while choice != 'X':
	if choice == 'W':
		amount = input("Input an amount to withdraw")
		account.withdraw(int(amount))
		print("Hello", account.name, "\tNuber: ", account.number, "\tBalance: ", account.balance)


	elif choice == 'D':
		amount = input("Input an amount to deposit")
		account.deposit(int(amount))
		print("Hello", account.name, "\tNuber: ", account.number, "\tBalance: ", account.balance)


	elif choice == 'I':
		account.add_interest()
		print("Hello", account.name, "\tNuber: ", account.number, "\tBalance: ", account.balance)


	elif choice == 'B':
		print(account.balance)
		print("Hello", account.name, "\tNuber: ", account.number, "\tBalance: ", account.balance)


	else:
		print('Invalid selection.')
	choice = input('Enter transaction selection: (W)withdrawl, (D)eposit, (I)nterest, (B)alance, e(X)it...')
	choice = choice.upper()




print("Thank you for using my bank")

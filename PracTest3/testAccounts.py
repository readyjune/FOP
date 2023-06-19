from accounts import BankAccount


def balances():
	try:
		print('\n#### Balances of All Accounts####\n')
		total = 0
		for i in range(len(my_accounts)):
			print("Name: ", my_accounts[i].name, "\tNumber: ", my_accounts[i].num, "\tBalance: ", my_accounts[i].bal)
			total = total + my_accounts[i].bal
		print("\t\t\t\t\tTotal: ", total)
	except SyntaxError:
		print("Error came out, you need to fix something")

print('\n#### Bank Accounts ####\n')
my_accounts = []

bank = BankAccount("Savings","200000-1", 2000)
my_accounts.append(bank)

bank = BankAccount("Everyday","200000-2", 200)
my_accounts.append(bank)

balances()
# add code for tasks here

print("\nDoing some transactions..\n")
my_accounts[0].deposit(200)
try:
	my_accounts[1].withdraw(20)
	my_accounts[1].withdraw(2000)
except ValueError as err:
	print("There are some errors in here", err)
my_accounts[0].add_interest()
my_accounts[1].add_interest()
my_accounts[0].charge_fees()
my_accounts[0].charge_fees()
my_accounts[1].charge_fees()
my_accounts[1].charge_fees()
balances()

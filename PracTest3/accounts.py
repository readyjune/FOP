class BankAccount():####class variable <BankAccount>
	interest_rate = 0.05
	def __init__(self, name, number, balance):
		self.name = name
		self.num = number
		self.bal = balance

	def withdraw(self, amount):####instance variable <withdraw>
		try:
			if amount > self.bal:
				raise Exception("Exception: Withdrawl exceeds balance.") #only self.bal is bigger than amount, and it goes down to the except Exception as e line.
				
			else:
				self.bal = self.bal - amount

		except Exception as e:
			print("Error is happened", e)  


	def deposit(self, amount):    #instance variable <deposit>
		self.bal = self.bal + amount

	def add_interest(self):     #instance variable <add_interest>
		self.bal += self.bal * self.interest_rate

	def charge_fees(self):	#instance variable <charge_fee>
		self.bal = self.bal - 5

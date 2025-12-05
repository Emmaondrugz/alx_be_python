class BankAccount:
	def __init__(self, initial_balance=0):
		self.initial_balance = initial_balance
	
	def deposit(self, amount):
		self.initial_balance += amount

	def withdraw(self, amount):
		if amount <= self.initial_balance:
			self.initial_balance -= amount
			return True
		else:
			return False

	def display_balance(self):
		print(f'Current Balance: $[self.initial_balance]')
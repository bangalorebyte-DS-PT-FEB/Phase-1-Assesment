class View:

	def type_user(self):
		type_ = input("Hi, there! Welcome to the stock trader app.\nNew User type 'n'\nExisting User type 'e'\n")
		return type_.lower()

	def username(self):
		username = input("Enter username\n")
		return username

	def password(self):
		pass_ = input("Enter password\n")
		return pass_


	def main_menu_admin(self, error = None):
		print("\033c")

		if error:
			print(error)

		print("To View Dashboard,enter 'L'\nPress 'X' to quit")

		return input('\n').lower().strip()

	def main_menu_user(self, error=None):
		print("\033c")

		if error:
			print(error)


		print("To Buy Stock,enter 'B'\nTo Sell Stock,enter 'S'\nTo View Dashboard,enter 'D'\nPress 'X' to quit")
		return input('? \n').lower().strip()


	def ticker(self, error=None):
		print("\033c")
		if error:
			print(error)
		ticker = input("To buy/sell stocks,please enter the ticker of the company:\n")
		return ticker

	def last_price(self, last_price, ticker):
		print("Price of " + str(ticker) + " : " + str(last_price) + " per share.")
		return input("Would you still like to continue to buy/sell the stock[y/n]?")

	def num_shares(self, ticker):
		return input("Enter the number of shares of " + str(ticker) + " you would like to buy/sell? \n")

	def buy(self, error=None):
		if error:
			print("You do not have enough money to complete this transaction. You will now return to the main menu.")


	def view_dashboard(self, dashboard):
		print("Your current account:")
		print(dashboard)

	def view_leaderboard(self, leaderboard):
		print("The leaderboard:")
		print(leaderboard)


	def exit(self):
		print("\033c")
		return input('Are you sure,you want to exit?[y/n]').strip()

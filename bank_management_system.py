class Account:
    def __init__(self, account_number, holder_name):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = 0

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount

    def get_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Account Number: {self.account_number} Holder: {self.holder_name} Balance: {self.balance}"
    

class SavingsAccount(Account):
    def __init__(self, account_number, holder_name, interest_rate):
        super().__init__(account_number, holder_name)
        self.interest_rate = interest_rate

    def add_interest(self):
        self.balance += self.balance * self.interest_rate / 100


class checkingAccount(Account):
    def __init__(self, account_number, holder_name, overdraft_limit):
        super().__init__(account_number, holder_name)
        self.overdraft_limit = overdraft_limit
        
    def withdraw(self, amount):
        if (0 < amount) and (amount <= self.balance + self.overdraft_limit):
            self.balance -= amount


class Bank:
    def __init__(self):
        self.accounts = []
    
    def add_account(self, account):
        self.accounts.append(account)

    def transfer(self, from_account, to_account, amount):
        if (from_account in self.accounts) and (to_account in self.accounts):
            if from_account.get_balance() >= amount:
                from_account.withdraw(amount)
                to_account.deposit(amount)

        print("from or to account are not present in the Accounts list")

    def display_accounts(self):
        for account in self.accounts:
            print(account)


def main():

    #Create bank
    bank = Bank()

    #Create accounts and add to bank
    savings = SavingsAccount("SA123", "Alice", 2.5)
    checking = checkingAccount("CA456", "Bob", 600)
    bank.add_account(savings)
    bank.add_account(checking)

    #Create transactions

    savings.deposit(1000)
    checking.deposit(500)

    savings. withdraw(200)
    checking.withdraw(200)

    savings.add_interest()

    bank.transfer(savings, checking, 300)

    #Display Accounts
    bank.display_accounts()


if __name__ == '__main__':
    main()
import account as ClassAccount

#_____________________________________________________________________________________________________#
# ユーザー情報を管理するクラス 
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.accounts = []

    def __str__(self):
        return f"User: {self.user_id}, Name: {self.name}"

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    
    def create_account(self, account_type, account_number, balance=0.0):
        if account_type == 'savings':
            account = ClassAccount.SavingsAccount(account_number, balance)
        elif account_type == 'checking':
            account = ClassAccount.CheckingAccount(account_number, balance)
        else:
            return False
        self.accounts.append(account)
        return True

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        return False
    
    def deposit(self, account_number, amount):
        account = self.get_account(account_number)
        msg = ""

        if account:
            if account.deposit(amount):
                msg = "Deposit successful!"
            else:
                msg = "Deposit failed!"
        else:
            msg = "Account not found!"
        return msg
    
    def withdraw(self, account_number, amount):
        account = self.get_account(account_number)
        msg = ""

        if account:
            if account.withdraw(amount):
                msg = "Withdrawal successful!"
            else:
                msg = "Withdrawal failed! Check your balance or overdraft limit."
        else:
            msg = "Account not found!"
        return msg
    
    def check_ok_to_transfer(self, account_number, amount, is_from_side):
        is_ok = False
        is_account_exist = False
        account = self.get_account(account_number)
        if account:
            is_ok = True
            is_account_exist = True
        else:
            pass
        return is_ok, is_account_exist
    
    def view_transaction_history(self, account_number):
        account = self.get_account(account_number)
        if account:
            for transaction in account.get_transaction_history():
                print(transaction)
        else:
            print("Account not found!")
        return

    def view_balance(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(f"Account Balance: {account.balance}")
        else:
            print("Account not found!")
        return
    
    def get_account_info(self, account_number):
        account = self.get_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")
        return
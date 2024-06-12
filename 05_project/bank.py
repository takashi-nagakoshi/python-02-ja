import account as ClassAccount
import user as ClassUser

#_____________________________________________________________________________________________________#
# Bank情報を管理するクラス 
class Bank:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = ClassUser.User(user_id, name)
            return True
        return False

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def create_account(self, user_id, account_type, account_number, balance=0.0):
        user = self.get_user(user_id)
        if user:
            if account_type == 'savings':
                account = ClassAccount.SavingsAccount(account_number, balance)
            elif account_type == 'checking':
                account = ClassAccount.CheckingAccount(account_number, balance)
            else:
                return False
            user.add_account(account)
            return True
        return False
    
    def delete_account(self, user_id, account_number):
        user = self.get_user(user_id)
        if not user:
            return False
        return user.delete_account(account_number)
    
    def deposit(self, user_id, account_number, amount):
        # 前処理と初期化
        user = self.get_user(user_id)

        # 本処理
        if user:
            account = user.get_account(account_number)
            if account:
                if account.deposit(amount):
                    print("Deposit successful!")
                else:
                    print("Deposit failed!")
            else:
                print("Account not found!")
        else:
            print("User not found!")
        return

    def withdraw(self, user_id, account_number, amount):
        # 前処理と初期化
        user = self.get_user(user_id)

        # 本処理
        if user:
            account = user.get_account(account_number)
            if account:
                if account.withdraw(amount):
                    print("Withdrawal successful!")
                else:
                    print("Withdrawal failed! Check your balance or overdraft limit.")
            else:
                print("Account not found!")
        else:
            print("User not found!")
        return
    
    def transfer(self, user_id_from, account_number_from, user_id_to, account_number_to, amount):
        # 前処理と初期化
        user_from = self.get_user(user_id_from)
        user_to = self.get_user(user_id_to)

        # 本処理
        if user_from and user_to:
            account_from = user_from.get_account(account_number_from)
            account_to = user_to.get_account(account_number_to)
            if account_from and account_to:
                if account_from.withdraw(amount):
                    account_to.deposit(amount)
                    print("Transfer successful!")
                else:
                    print("Transfer failed! Check your balance or overdraft limit.")
            else:
                print("One or both accounts not found!")
        else:
            print("One or both users not found!")
        return

    def view_transaction_history(self, user_id, account_number):
        # 前処理と初期化
        user = self.get_user(user_id)

        # 本処理
        if user:
            account = user.get_account(account_number)
            if account:
                for transaction in account.get_transaction_history():
                    print(transaction)
            else:
                print("Account not found!")
        else:
            print("User not found!")
        return

    def view_balance(self, user_id, account_number):
        # 前処理と初期化
        user = self.get_user(user_id)

        # 本処理
        if user:
            account = user.get_account(account_number)
            if account:
                print(f"Account Balance: {account.balance}")
            else:
                print("Account not found!")
        else:
            print("User not found!")
        return
    
    def get_account_info(self, user_id, account_number):
        # 前処理と初期化
        user = self.get_user(user_id)

        # 本処理
        if user:
            account = user.get_account(account_number)
            if account:
                print(account)
            else:
                print("Account not found!")
        else:
            print("User not found!")
        return

        


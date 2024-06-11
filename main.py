from abc import ABC, abstractmethod
#初期化　口座番号、残高、取引履歴
class Account(ABC):
    def __init__(self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

#抽象メソッド 
    @abstractmethod
    def can_withdraw(self, amount):
        pass   
    #指定された金額をアカウントに預金
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transaction_history.append(f"Deposited {amount}")
            return f"Deposited {amount}. New balance: {self.balance}"
    #can_withdraw(amount) に基づいて引き出し
    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Withdrawal denied. Insufficient funds or rules not met."
    #利息を適用するためのメソッドで、サブクラスで上書き　？この場所にいるのか？
    def apply_interest(self):
        pass
    #取引履歴
    def get_transaction_history(self):
        return self.transaction_history
    #口座情報を文字列で返す
    def __str__(self):
        return f"Account: {self.account_number}, Balance: {self.balance}"
# Accountクラスを継承   貯蓄口座
class SavingsAccount(Account):
    # 初期化
    def __init__(self, account_number, balance=0, interest_rate=0.01):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate
    # 残高が引き出し金額以上であれば可能
    def can_withdraw(self, amount):
        return self.balance >= amount
    # 金利を計算し、残高に追加します。また、取引履歴にも追加
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.transaction_history.append(f"Interest applied: {interest}")
        return f"Interest applied: {interest}. New balance: {self.balance}"
    # 貯蓄口座情報を文字列で返す
    def __str__(self):
        return f"Savings Account: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"
# 当座預金口座
class CheckingAccount(Account):
    def __init__(self, account_number, balance=0, interest_rate=0.02):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def can_withdraw(self, amount):
        return self.balance + self.interest_rate >= amount
    
    def __str__(self):
        return f"Checking Account: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"
# ユーザー情報を管理するクラス 
class User:
    def __init__(self, user_id, name):
        self.user_id = user_id
        self.name = name
        self.accounts = []

    def add_account(self, account):
        self.accounts.append(account)

    def delete_account(self, account_number):
        if account_number in self.accounts:
            del self.accounts[account_number]
            return True
        return False

    def get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None

    def __str__(self):
        return f"User: {self.user_id}, Name: {self.name}"
# Bank情報を管理するクラス 
class Bank:
    def __init__(self):
        self.users = {}

    def create_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = User(user_id, name)
            return True
        return False

    def get_user(self, user_id):
        return self.users.get(user_id, None)

    def create_account(self, user_id, account_type, account_number, balance=0.0):
        user = self.get_user(user_id)
        if user:
            if account_type == 'savings':
                account = SavingsAccount(account_number, balance)
            elif account_type == 'checking':
                account = CheckingAccount(account_number, balance)
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
    
# BankingSystem クラス   
class BankingSystem:
    def __init__(self):
        self.bank = Bank()

    def run(self):
        while True:
            print("\nBanking System Menu:")
            print("1. Create User")
            print("2. Create Account")
            print("3. Deposit")
            print("4. Withdraw")
            print("5. Transfer")
            print("6. View Transaction History")
            print("7. View Balance")
            print("8. Delete Account")
            print("9. Get Account Info")
            print("10. Quit")
            choice = input("Enter choice: ")

            if choice == '1':
                self.create_user()
            elif choice == '2':
                self.create_account()
            elif choice == '3':
                self.deposit()
            elif choice == '4':
                self.withdraw()
            elif choice == '5':
                self.transfer()
            elif choice == '6':
                self.view_transaction_history()
            elif choice == '7':
                self.view_balance()
            elif choice == '8':
                self.delete_account()
            elif choice == '9':
                self.get_account_info()
            elif choice == '10':
                break
            else:
                print("Invalid choice!")
#1ユーザーid と名前
    def create_user(self):
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")
        if self.bank.create_user(user_id, name):
            print("User created successfully!")
        else:
            print("User already exists!")
#2口座の開設　パスワード
    def create_account(self):
        user_id = input("Enter user ID: ")
        account_type = input("Enter account type (savings/checking): ")
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))
        if self.bank.create_account(user_id, account_type, account_number, balance):
            print("Account created successfully!")
        else:
            print("Failed to create account!")
#3入金
    def deposit(self):
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))
        user = self.bank.get_user(user_id)
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
#4出金
    def withdraw(self):
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))
        user = self.bank.get_user(user_id)
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
#5送金
    def transfer(self):
        user_id_from = input("Enter sender user ID: ")
        account_number_from = input("Enter sender account number: ")
        user_id_to = input("Enter recipient user ID: ")
        account_number_to = input("Enter recipient account number: ")
        amount = float(input("Enter amount to transfer: "))
        user_from = self.bank.get_user(user_id_from)
        user_to = self.bank.get_user(user_id_to)
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
#6履歴
    def view_transaction_history(self):
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        user = self.bank.get_user(user_id)
        if user:
            account = user.get_account(account_number)
            if account:
                for transaction in account.get_transaction_history():
                    print(transaction)
            else:
                print("Account not found!")
        else:
            print("User not found!")
#7口座残高
    def view_balance(self):
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        user = self.bank.get_user(user_id)
        if user:
            account = user.get_account(account_number)
            if account:
                print(f"Account Balance: {account.balance}")
            else:
                print("Account not found!")
        else:
            print("User not found!")
#8口座解約
    def delete_account(self):
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        if self.bank.delete_account(user_id, account_number):
            print("Account deleted successfully!")
        else:
            print("Failed to delete account!")
#9口座情報
    def get_account_info(self):
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        user = self.bank.get_user(user_id)
        if user:
            account = user.get_account(account_number)
            if account:
                print(account)
            else:
                print("Account not found!")
        else:
            print("User not found!")

# 実行       
if __name__ == "__main__":
    banking_system = BankingSystem()
    banking_system.run()

#?8で口座消したけど　9で残る
 
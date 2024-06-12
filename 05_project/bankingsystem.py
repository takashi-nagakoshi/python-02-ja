import bank as ClassBank
    
#_____________________________________________________________________________________________________#
# BankingSystem クラス   
class BankingSystem:
    def __init__(self):
        self.bank = ClassBank.Bank()

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
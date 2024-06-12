import bank as ClassBank

KEY_CREATE_USER         = "1"
KEY_CREATE_ACCOUNT      = "2"
KEY_DEPOSIT             = "3"
KEY_WITHDRAW            = "4"
KEY_TRANSFER            = "5"
KEY_VIEW_TRANS_HISTORY  = "6"
KEY_VIEW_BALANCE        = "7"
KEY_DELETE_ACCOUNT      = "8"
KEY_GET_ACCOUNT_INFO    = "9"
KEY_QUIT                = "10"

#_____________________________________________________________________________________________________#
# BankingSystem クラス   
class BankingSystem:
    def __init__(self):
        self.bank = ClassBank.Bank()

    def run(self):
        while True:
            print("############### Banking System Menu ###############")
            print(KEY_CREATE_USER        + ". Create User")
            print(KEY_CREATE_ACCOUNT     + ". Create Account")
            print(KEY_DEPOSIT            + ". Deposit")
            print(KEY_WITHDRAW           + ". Withdraw")
            print(KEY_TRANSFER           + ". Transfer")
            print(KEY_VIEW_TRANS_HISTORY + ". View Transaction History")
            print(KEY_VIEW_BALANCE       + ". View Balance")
            print(KEY_DELETE_ACCOUNT     + ". Delete Account")
            print(KEY_GET_ACCOUNT_INFO   + ". Get Account Info")
            print(KEY_QUIT               + ". Quit")
            choice = input("Enter choice: ")

            if choice == KEY_CREATE_USER:
                self.create_user()
            elif choice == KEY_CREATE_ACCOUNT:
                self.create_account()
            elif choice == KEY_DEPOSIT:
                self.deposit()
            elif choice == KEY_WITHDRAW:
                self.withdraw()
            elif choice == KEY_TRANSFER:
                self.transfer()
            elif choice == KEY_VIEW_TRANS_HISTORY:
                self.view_transaction_history()
            elif choice == KEY_VIEW_BALANCE:
                self.view_balance()
            elif choice == KEY_DELETE_ACCOUNT:
                self.delete_account()
            elif choice == KEY_GET_ACCOUNT_INFO:
                self.get_account_info()
            elif choice == KEY_QUIT:
                break
            else:
                print("Invalid choice!")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # ユーザの登録
    def create_user(self):
        # ユーザー入力
        user_id = input("Enter user ID: ")
        name = input("Enter user name: ")

        # ユーザ登録処理
        if self.bank.create_user(user_id, name):
            print("User created successfully!")
        else:
            print("User already exists!")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の開設
    def create_account(self):
        # ユーザ入力
        user_id = input("Enter user ID: ")
        account_type = input("Enter account type (savings/checking): ")
        account_number = input("Enter account number: ")
        balance = float(input("Enter initial balance: "))

        # 口座開設処理
        if self.bank.create_account(user_id, account_type, account_number, balance):
            print("Account created successfully!")
        else:
            print("Failed to create account!")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座への入金
    def deposit(self):
        # ユーザ入力
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to deposit: "))

        # 入金処理
        self.bank.deposit(user_id, account_number, amount)

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座からの出金
    def withdraw(self):
        # ユーザ入力
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        amount = float(input("Enter amount to withdraw: "))

        # 出金処理
        self.bank.withdraw(user_id, account_number, amount)

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座から別口座への送金
    def transfer(self):
        # ユーザ入力：送金元の情報
        user_id_from = input("Enter sender user ID: ")
        account_number_from = input("Enter sender account number: ")

        # ユーザ入力：送金先の情報
        user_id_to = input("Enter recipient user ID: ")
        account_number_to = input("Enter recipient account number: ")

        # ユーザ入力：送金額の情報
        amount = float(input("Enter amount to transfer: "))

        # 送金処理
        self.bank.transfer(user_id_from, account_number_from, user_id_to, account_number_to, amount)
        return

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の取引履歴を表示
    def view_transaction_history(self):
        # ユーザ入力
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")
        
        # 取引履歴取得処理
        self.bank.view_transaction_history(user_id, account_number)
        return

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の残高を表示
    def view_balance(self):
        # ユーザ入力
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")

        # 口座残高取得処理
        self.bank.view_balance(user_id, account_number)
        return

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座を解約(消去)
    def delete_account(self):
        # ユーザ処理
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")

        # 口座消去処理
        if self.bank.delete_account(user_id, account_number):
            print("Account deleted successfully!")
        else:
            print("Failed to delete account!")
        return

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の情報を表示
    def get_account_info(self):
        # ユーザ処理
        user_id = input("Enter user ID: ")
        account_number = input("Enter account number: ")

        # 口座情報取得
        self.bank.get_account_info(user_id, account_number)
        return
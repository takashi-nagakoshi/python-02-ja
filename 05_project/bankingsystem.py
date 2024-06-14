import bank as ClassBank

KEY_LOGIN_USER          = "1"
KEY_CREATE_USER         = "2"

KEY_CREATE_ACCOUNT      = "0"
KEY_DEPOSIT             = "1"
KEY_WITHDRAW            = "2"
KEY_TRANSFER            = "3"
KEY_VIEW_TRANS_HISTORY  = "4"
KEY_VIEW_BALANCE        = "5"
KEY_GET_ACCOUNT_INFO    = "6"
KEY_DELETE_ACCOUNT      = "7"
KEY_QUIT                = "X"
WAIT_ROW = "....."

#_____________________________________________________________________________________________________#
# BankingSystem クラス   
class BankingSystem:
    def __init__(self):
        self.bank = ClassBank.Bank()

    def run(self):
        # Main menu 
        while True:
            print("")
            print("############### Banking System Menu ###############")
            print("### Main menu")
            print(KEY_LOGIN_USER         + ". Login User")
            print(KEY_CREATE_USER        + ". Create User")
            print(KEY_QUIT               + ". Quit")
            print(WAIT_ROW)
            choice = input("Enter choice: ")

            if choice == KEY_CREATE_USER:
                self.create_user()
            elif choice == KEY_LOGIN_USER:
                user_id = self.login_user()
                if user_id:
                    self.run_user_menu(user_id)
                else:
                    continue
            elif choice == KEY_QUIT:
                break
            else:
                print("Invalid choice!")
        return
    
    def login_user(self):
        count = 0 # 同じ入力を何回システムから聞き返したか
        count_max = 3 # 最大何回まで同じ入力をシステムから聞き返すか

        # ユーザーIDの確認
        while True:
            user_id = input("Enter user ID: ")
            is_use_id_exist = self.bank.check_user_id_exist(user_id)
            if is_use_id_exist:
                break
            else:
                count += 1
                if count < count_max:
                    print("... That user ID doesn't exist.")
                    continue
                else:
                    print("... User login failed")
                    return None
        
        # パスワードの確認
        count = 0
        while True:
            user_passwd = input("Enter user password: ")
            is_passwd_correct = self.bank.check_user_id_and_password_are_correct(user_id, user_passwd)
            if is_passwd_correct:
                print("... Login success")
                return user_id
            else:
                count += 1
                if count < count_max:
                    print("... Incorrect password.")
                    continue
                else:
                    print("... User login failed")
                    return None


    def run_user_menu(self, user_id):
        while True:
            print("")
            print("############### Banking System Menu ###############")
            print("### User menu (user_id = " + user_id + ")")
            print(KEY_CREATE_ACCOUNT     + ". Create Account")
            print(" --  --  --  --  --  -- ")
            print(KEY_DEPOSIT            + ". Deposit")
            print(KEY_WITHDRAW           + ". Withdraw")
            print(KEY_TRANSFER           + ". Transfer")
            print(" --  --  --  --  --  -- ")
            print(KEY_VIEW_TRANS_HISTORY + ". View Transaction History")
            print(KEY_VIEW_BALANCE       + ". View Balance")
            print(KEY_GET_ACCOUNT_INFO   + ". Get Account Info")
            print(" --  --  --  --  --  -- ")
            print(KEY_DELETE_ACCOUNT     + ". Delete Account")
            print(KEY_QUIT               + ". Quit")
            print(WAIT_ROW)
            choice = input("Enter choice: ")

            if choice == KEY_CREATE_ACCOUNT:
                self.create_account()
            elif choice == KEY_DEPOSIT:
                self.deposit(user_id)
            elif choice == KEY_WITHDRAW:
                self.withdraw(user_id)
            elif choice == KEY_TRANSFER:
                self.transfer(user_id)
            elif choice == KEY_VIEW_TRANS_HISTORY:
                self.view_transaction_history(user_id)
            elif choice == KEY_VIEW_BALANCE:
                self.view_balance(user_id)
            elif choice == KEY_GET_ACCOUNT_INFO:
                self.get_account_info(user_id)
            elif choice == KEY_DELETE_ACCOUNT:
                self.delete_account(user_id)
            elif choice == KEY_QUIT:
                break
            else:
                print("Invalid choice!")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # ユーザの登録
    def create_user(self):
        try:
            # ユーザー入力
            user_id = input("Enter user ID: ")
            name = input("Enter user name: ")
            passwd = input("Enter user password: ")
            print(WAIT_ROW)

            # ユーザ登録処理
            if self.bank.create_user(user_id, name, passwd):
                print("User created successfully!")
            else:
                print("User already exists!")
        except Exception as e:
            print(f"Error creating user: {e}")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の開設
    def create_account(self):
        try:
            # ユーザ入力
            user_id = input("Enter user ID: ")
            account_type = input("Enter account type (savings/checking): ")
            account_number = input("Enter account number: ")
            balance = float(input("Enter initial balance: "))
            print(WAIT_ROW)

            # 口座開設処理
            if self.bank.create_account(user_id, account_type, account_number, balance):
                print("Account created successfully!")
            else:
                print("Failed to create account!")
        except ValueError as e:
            print(f"Invalid input: {e}")
        except Exception as e:
            print(f"Error creating account: {e}")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座への入金
    def deposit(self, user_id):
        # ユーザ入力
        try:
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to deposit: "))
            print(WAIT_ROW)

            # 入金処理
            self.bank.deposit(user_id, account_number, amount)
        except (ValueError):
            print("Invalid amount entered.")
        except UnboundLocalError:
            print("Error: 'UnboundLocalError deposit4.")


    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座からの出金
    def withdraw(self, user_id):
        try:
            # ユーザ入力
            account_number = input("Enter account number: ")
            amount = float(input("Enter amount to withdraw: "))
            print(WAIT_ROW)

            # 出金処理
            self.bank.withdraw(user_id, account_number, amount)
        except ValueError as e:
            print(f"Invalid amount entered: {e}")
        except Exception as e:
            print(f"Error during withdrawal: {e}")


    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座から別口座への送金
    def transfer(self, user_id_from):
        try:
            # ユーザ入力：送金元の情報
            account_number_from = input("Enter sender account number: ")

            # ユーザ入力：送金先の情報
            user_id_to = input("Enter recipient user ID: ")
            account_number_to = input("Enter recipient account number: ")

            # ユーザ入力：送金額の情報
            amount = float(input("Enter amount to transfer: "))
            print(WAIT_ROW)

            # 送金処理
            self.bank.transfer(user_id_from, account_number_from, user_id_to, account_number_to, amount)
            return
        except ValueError as e:
            print(f"Invalid amount entered: {e}")
        except Exception as e:
            print(f"Error during transfer: {e}")


    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の取引履歴を表示
    def view_transaction_history(self, user_id):
        try:
            # ユーザ入力
            account_number = input("Enter account number: ")
            print(WAIT_ROW)
            
            # 取引履歴取得処理
            self.bank.view_transaction_history(user_id, account_number)
            return
        except Exception as e:
            print(f"Error viewing transaction history: {e}")

    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の残高を表示
    def view_balance(self, user_id):
        try:
            # ユーザ入力
            account_number = input("Enter account number: ")
            print(WAIT_ROW)

            # 口座残高取得処理
            self.bank.view_balance(user_id, account_number)
            return
        except Exception as e:
            print(f"Error viewing balance: {e}")
    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座を解約(消去)
    def delete_account(self, user_id):
        try:
            # ユーザ処理
            account_number = input("Enter account number: ")
            print(WAIT_ROW)

            # 口座消去処理
            if self.bank.delete_account(user_id, account_number):
                print("Account deleted successfully!")
            else:
                print("Failed to delete account!")
            return
        except Exception as e:
            print(f"Error deleting account: {e}")
    #\__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ \__ 
    # 口座の情報を表示
    def get_account_info(self, user_id):
        try:
            # ユーザ処理
            account_number = input("Enter account number: ")
            print(WAIT_ROW)

            # 口座情報取得
            self.bank.get_account_info(user_id, account_number)
            return
        except Exception as e:
            print(f"Error getting account info: {e}")
import account as ClassAccount

#_____________________________________________________________________________________________________#
# ユーザー情報を管理するクラス 
class User:
    def __init__(self, user_id, name, passwd):
        self.user_id = user_id
        self.name = name
        self.__passwd = passwd
        self.accounts = []

    def __str__(self):
        return f"User: {self.user_id}, Name: {self.name}"

    def __get_account(self, account_number):
        for account in self.accounts:
            if account.account_number == account_number:
                return account
        return None
    # 口座番号は数字だけに限定し，その上で上限桁数を設定する
    def is_valid_account_number(self, account_number, max_length=10):
        return account_number.isdigit() and len(account_number) <= max_length

    def check_account_number_already_exist(self, account_number):
        account = self.__get_account(account_number)
        if account:
            return True
        else:
            return False

    def create_account(self, account_type, account_number, balance=0.0):
        # 追加部分: 口座番号が有効かどうかをチェック
        if not self.is_valid_account_number(account_number):
            print("Invalid account number! It must be numeric and up to 10 digits long.")  
            return False
        
        account = self.__get_account(account_number)
        if account:
            # 既に同一IDのアカウントがあるとき，口座を追加しないようにする．
            return False
        else:
            if account_type == 'savings':
                account = ClassAccount.SavingsAccount(account_number, balance)
            elif account_type == 'checking':
                account = ClassAccount.CheckingAccount(account_number, balance)
            else:
                return False
        self.accounts.append(account)
        return True

    def delete_account(self, account_number):
        account = self.__get_account(account_number)
        if account:
            self.accounts.remove(account)
            return True
        return False
    
    def deposit(self, account_number, amount):
        account = self.__get_account(account_number)
        msg = ""

        try:
            if account:
                if account.deposit(amount):
                    msg = "Deposit successful!"
                else:
                    msg = "Deposit failed!"
            else:
                msg = "Account not found!"
            return msg
        except (ValueError):
            print("Invalid amount entered.")
        except UnboundLocalError:
            print("Error: 'UnboundLocalError deposit2.")

    def withdraw(self, account_number, amount):
        account = self.__get_account(account_number)
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
        account = self.__get_account(account_number)
        if account:
            is_account_exist = True
            if is_from_side:
                if account.can_withdraw(amount):
                    is_ok = True
            else:
                is_ok = True
        else:
            pass
        return is_ok, is_account_exist
    
    def view_transaction_history(self, account_number):
        account = self.__get_account(account_number)
        if account:
            for transaction in account.get_transaction_history():
                print(transaction)
        else:
            print("Account not found!")
        return

    def view_balance(self, account_number):
        account = self.__get_account(account_number)
        if account:
            print(f"Account Balance: {account.balance}")
        else:
            print("Account not found!")
        return
    
    def get_account_info(self, account_number):
        account = self.__get_account(account_number)
        if account:
            print(account)
        else:
            print("Account not found!")
        return
    
    def check_passwd_is_correct(self, passwd):
        return self.__passwd == passwd
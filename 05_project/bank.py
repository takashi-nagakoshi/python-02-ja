import account as ClassAccount
import user as ClassUser

#_____________________________________________________________________________________________________#
# Bank情報を管理するクラス 
class Bank:
    def __init__(self):
        self.users = {}

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def __get_user(self, user_id):
        return self.users.get(user_id, None)

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def create_user(self, user_id, name):
        if user_id not in self.users:
            self.users[user_id] = ClassUser.User(user_id, name)
            return True
        return False

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def create_account(self, user_id, account_type, account_number, balance=0.0):
        user = self.__get_user(user_id)
        return user.create_account(account_type, account_number, balance)
    
    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def delete_account(self, user_id, account_number):
        user = self.__get_user(user_id)
        if not user:
            return False
        return user.delete_account(account_number)

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def deposit(self, user_id, account_number, amount):
        user = self.__get_user(user_id)
        if user:
            msg = user.deposit(account_number, amount)
            print(msg)
        else:
            print("User not found!")
        return

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def withdraw(self, user_id, account_number, amount):
        user = self.__get_user(user_id)
        if user:
            msg = user.withdraw(account_number, amount)
            print(msg)
        else:
            print("User not found!")
        return
    
    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def transfer(self, user_id_from, account_number_from, user_id_to, account_number_to, amount):
        # 前処理と初期化
        user_f = self.__get_user(user_id_from)
        user_t = self.__get_user(user_id_to)

        # 本処理
        if user_f and user_t:    
            is_ok_f, is_account_exist_f = user_f.check_ok_to_transfer(account_number_from, amount, True)
            is_ok_t, is_account_exist_t = user_t.check_ok_to_transfer(account_number_from, amount, False)
            if is_ok_f and is_ok_t:
                user_f.withdraw(account_number_from, amount)
                user_t.deposit(account_number_to, amount)
                print("Transfer successful!")
            elif (not is_account_exist_f) and (not is_account_exist_t):
                print("Transfer failed! Check your balance or overdraft limit.")
            else:
                print("One or both accounts not found!")
        else:
            print("One or both users not found!")
        return

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def view_transaction_history(self, user_id, account_number):
        user = self.__get_user(user_id)
        if user:
            user.view_transaction_history(account_number)
        else:
            print("User not found!")
        return

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def view_balance(self, user_id, account_number):
        user = self.__get_user(user_id)
        if user:
            user.view_balance(account_number)
        else:
            print("User not found!")
        return
    
    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def get_account_info(self, user_id, account_number):
        user = self.__get_user(user_id)
        if user:
            user.get_account_info(account_number)
        else:
            print("User not found!")
        return

        


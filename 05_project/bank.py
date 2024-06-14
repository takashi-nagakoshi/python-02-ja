import user as ClassUser

#_____________________________________________________________________________________________________#
# Bank情報を管理するクラス 
class Bank:
    def __init__(self):
        self.users = []

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def __get_user(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user
        return None

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def create_user(self, user_id, name, passwd):
        existing_user = self.__get_user(user_id)
        if existing_user:
            return False
        else:
            new_user = ClassUser.User(user_id, name, passwd)
            self.users.append(new_user)
            return True

    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def create_account(self, user_id, account_type, account_number, balance=0.0):
        for user in self.users:
            if user.check_account_number_already_exist(account_number):
                return False
        
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
        try:
            if user:
                msg = user.deposit(account_number, amount)
                print(msg)
            else:
                print("User not found!")
            return
        except (ValueError):
            print("Invalid amount entered.")
        except UnboundLocalError:
            print("Error: 'UnboundLocalError deposit3.")

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
            is_ok_t, is_account_exist_t = user_t.check_ok_to_transfer(account_number_to, amount, False)
            if is_ok_f and is_ok_t:
                msg = user_f.withdraw(account_number_from, amount)
                msg = user_t.deposit(account_number_to, amount)
                # 返り値で得られるmsgは使わない．
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
    
    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def check_user_id_exist(self, user_id):
        user = self.__get_user(user_id)
        if user:
            return True
        else:
            return False
        
    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def check_user_id_and_password_are_correct(self, user_id, passwd):
        user = self.__get_user(user_id)
        if user:
            return user.check_passwd_is_correct(passwd)
        else:
            return False
    
    #___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ ___ 
    def check_account_number_exist(self, user_id, account_number):
        user = self.__get_user(user_id)
        if user:
            return user.check_account_number_exist(account_number)
        else:
            return False

        


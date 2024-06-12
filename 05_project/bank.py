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
        print("#######################" + account_type)
        if user:
            if account_type == 'savings':
                account = ClassAccount.SavingsAccount(account_number, balance)
            elif account_type == 'checking':
                account = ClassAccount.CheckingAccount(account_number, balance)
            else:
                print("%%%%%%%%%%%%%%%%%%%%%% aaaaa")
                return False
            user.add_account(account)
            return True
        print("%%%%%%%%%%%%%%%%%%%%%% bbbbb")
        return False
    
    def delete_account(self, user_id, account_number):
        user = self.get_user(user_id)
        if not user:
            return False
        return user.delete_account(account_number)
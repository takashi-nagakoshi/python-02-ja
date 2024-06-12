import account as ClassAccount

#_____________________________________________________________________________________________________#
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
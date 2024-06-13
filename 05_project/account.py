from abc import ABC, abstractmethod
#_____________________________________________________________________________________________________#
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
        try:
            if amount > 0:
                self.balance += amount
                self.transaction_history.append(f"Deposited {amount}")
                return f"Deposited {amount}. New balance: {self.balance}"
        except ValueError:
            print("Invalid amount entered.")
        except UnboundLocalError:
            print("Error: 'UnboundLocalError deposit1.")


    #can_withdraw(amount) に基づいて引き出し
    def withdraw(self, amount):
        if self.can_withdraw(amount):
            self.balance -= amount
            self.transaction_history.append(f"Withdrew {amount}")
            return f"Withdrew {amount}. New balance: {self.balance}"
        else:
            return "Withdrawal denied. Insufficient funds or rules not met."

    #取引履歴
    def get_transaction_history(self):
        return self.transaction_history

    #口座情報を文字列で返す
    def __str__(self):
        return f"Account: {self.account_number}, Balance: {self.balance}"

#_____________________________________________________________________________________________________#
# Accountクラスを継承   貯蓄口座
class SavingsAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)
    
    # 残高が引き出し金額以上であれば可能
    def can_withdraw(self, amount):
        return self.balance >= amount
    
    # 貯蓄口座情報を文字列で返す
    def __str__(self):
        return f"Savings Account: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"

#_____________________________________________________________________________________________________#
# 当座預金口座
class CheckingAccount(Account):
    def __init__(self, account_number, balance=0):
        super().__init__(account_number, balance)

    def can_withdraw(self, amount):
        # interest(利息)を考慮すればSavingAccountと処理が変わる可能性があるが，現状簡略のためSavingAccountと同じ処理になっている．
        return self.balance >= amount
    
    def __str__(self):
        return f"Checking Account: {self.account_number}, Balance: {self.balance}, Interest Rate: {self.interest_rate}"
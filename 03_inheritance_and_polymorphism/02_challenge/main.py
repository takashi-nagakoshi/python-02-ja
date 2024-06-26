from abc import ABC, abstractmethod
#初期化　口座番号、残高、取引履歴
class Account(ABC):
    def __init__(self,account_number,balance=0):
        self.account_number = account_number
        self.balance = balance
        self.transaction_history = []

#抽象メソッド ？何の意味があるのか？
    @abstractmethod
    def can_withdraw(self, amount):
        pass   
    #指定された金額をアカウントに入金
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

alice_savings = SavingsAccount("123456", 1000)
bob_checking = CheckingAccount("987654", 500)

accounts = [alice_savings, bob_checking]

print("Initial Account Details:")
print(alice_savings)
print(bob_checking)

print(alice_savings.deposit(200))
print(alice_savings.withdraw(500))
print(bob_checking.deposit(300))
print(bob_checking.withdraw(1000))

print(alice_savings.get_transaction_history())
print(bob_checking.get_transaction_history())

print(alice_savings)
print(bob_checking)   
import unittest
from account import SavingsAccount, CheckingAccount

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.savings_account = SavingsAccount('1234567890', 1000.0)
        self.checking_account = CheckingAccount('0987654321', 1000.0)

    def test_can_withdraw(self):
        self.assertTrue(self.savings_account.can_withdraw(500))
        self.assertFalse(self.savings_account.can_withdraw(1500))
        self.assertTrue(self.checking_account.can_withdraw(500))
        self.assertFalse(self.checking_account.can_withdraw(1500))

    def test_deposit(self):
        self.assertEqual(self.savings_account.deposit(500), "Deposited 500. New balance: 1500.0")
        self.assertEqual(self.checking_account.deposit(500), "Deposited 500. New balance: 1500.0")

    def test_withdraw(self):
        self.assertEqual(self.savings_account.withdraw(500), "Withdrew 500. New balance: 500.0")
        self.assertEqual(self.savings_account.withdraw(1500), "Withdrawal denied. Insufficient funds or rules not met.")
        self.assertEqual(self.checking_account.withdraw(500), "Withdrew 500. New balance: 500.0")
        self.assertEqual(self.checking_account.withdraw(1500), "Withdrawal denied. Insufficient funds or rules not met.")

    def test_get_transaction_history(self):
        self.savings_account.deposit(500)
        self.savings_account.withdraw(500)
        self.assertEqual(self.savings_account.get_transaction_history(), ["Deposited 500", "Withdrew 500"])

    def test_str(self):
        self.assertEqual(str(self.savings_account), "Savings Account: 1234567890, Balance: 1000.0")
        self.assertEqual(str(self.checking_account), "Checking Account: 0987654321, Balance: 1000.0")

if __name__ == "__main__":
    unittest.main()
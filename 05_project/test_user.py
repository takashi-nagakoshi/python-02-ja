import unittest
from user import User  # your_moduleを実際のモジュール名に置き換えてください

class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User('123', 'Test User')

    def test_create_account(self):
        self.assertTrue(self.user.create_account('savings', '1234567890', 1000.0))
        self.assertFalse(self.user.create_account('savings', '1234567890', 1000.0))
        self.assertFalse(self.user.create_account('savings', '1234567890a', 1000.0))
        self.assertFalse(self.user.create_account('savings', '12345678901', 1000.0))

    #def test_delete_account(self):
    #    self.user.create_account('savings', '1234567890', 1000.0)
    #    self.assertTrue(self.user.delete_account('1234567890'))
    #    self.assertFalse(self.user.delete_account('1234567891'))

    def test_deposit(self):
        self.user.create_account('savings', '1234567890', 1000.0)
        self.assertEqual(self.user.deposit('1234567890', 500), "Deposit successful!")
        self.assertEqual(self.user.deposit('0987654321', 500), "Account not found!")
        #with self.assertRaises(ValueError):
        #    self.user.deposit('1234567890', -500)

   # def test_withdraw(self):
   #     self.user.create_account('savings', '1234567890', 1000.0)
   #     self.assertEqual(self.user.withdraw('1234567890', 500), "Withdrawal successful!")
   #     self.assertEqual(self.user.withdraw('1234567890', 1500), "Withdrawal failed! Check your balance or overdraft limit.")
   #     self.assertEqual(self.user.withdraw('0987654321', 500), "Account not found!")

    def test_check_ok_to_transfer(self):
        self.user.create_account('savings', '1234567890', 1000.0)
        self.assertEqual(self.user.check_ok_to_transfer('1234567890', 500, True), (True, True))
        self.assertEqual(self.user.check_ok_to_transfer('1234567890', 1500, True), (False, True))
        self.assertEqual(self.user.check_ok_to_transfer('0987654321', 500, True), (False, False))

    #def test_view_balance(self):
    #    self.user.create_account('savings', '1234567890', 1000.0)
    #    self.assertEqual(self.user.view_balance('1234567890'), 1000.0)
    #    self.assertEqual(self.user.view_balance('0987654321'), "Account not found!")

    #def test_get_account_info(self):
    #    self.user.create_account('savings', '1234567890', 1000.0)
    #    self.assertEqual(self.user.get_account_info('1234567890'), "savings account 1234567890")  
    #    self.assertEqual(self.user.get_account_info('0987654321'), "Account not found!")

if __name__ == "__main__":
    unittest.main()
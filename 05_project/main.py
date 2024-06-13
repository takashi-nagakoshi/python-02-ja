import bankingsystem as ClassBankingSystem

if __name__ == "__main__":
    try:
        banking_system = ClassBankingSystem.BankingSystem()
        banking_system.run()
    except ValueError:
        print("Error: 'valueError.")
    except UnboundLocalError:
        print("Error: 'UnboundLocalError.")
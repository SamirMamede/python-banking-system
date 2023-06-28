class BankAccount:
    def __init__(self, account_number, initial_balance=0):
        self.account_number = account_number
        self.balance = initial_balance
        self.deposit_count = 0
        self.withdrawal_count = 0

    def deposit(self, amount):
        amount = int(input("Qual o valor do depósito: "))
        if amount > 0:
            self.balance += amount
            self.deposit_count +=1
            print(f"Depositou R${amount:.2f} na conta {self.account_number}.")
        else:
            print("Valor inserido inválido. O valor do depósito deve ser maior que 0.")

    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                self.withdrawal_count += 1
                print(f"Saque de R${amount:.2f} realizado com sucesso!")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor inserido inválido. O valor da retirada deve ser maior que 0.")

    def extract(self):
        print(f"Número da conta: {self.account_number}")
        print(f"Saldo: R${self.balance:.2f}")
        print(f"Número de depósitos realizados: {self.deposit_count}")
        print(f"Número de saques realizados: {self.withdrawal_count}")


account1 = BankAccount("12345", 0)
account1.deposit(500)
account1.withdraw(200)
account1.extract()

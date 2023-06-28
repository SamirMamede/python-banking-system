import datetime

class BankAccount:
    def __init__(self):
        self.balance = 0
        self.deposit_count = 0
        self.withdrawal_count = 0
        self.last_withdrawal_date = None

    def deposit(self):
        amount = int(input("Qual o valor do depósito: "))
        if amount > 0:
            self.balance += amount
            self.deposit_count +=1
            print(f"Depositou R${amount:.2f}")
        else:
            print("Valor inserido inválido. O valor do depósito deve ser maior que 0.")

    def withdraw(self):
        amount = int(input("Qual o valor do saque? "))
        if amount > 0:
            if self.balance >= amount:
                today = datetime.date.today()
                if self.last_withdrawal_date != today:
                    self.withdrawal_count = 0
                    self.last_withdrawal_date = today

                if self.withdrawal_count < 3:
                    if amount <= 500.0:
                        self.balance -= amount
                        self.withdrawal_count += 1
                        print(f"Saque de R${amount:.2f} bem sucedido!")
                    else:
                        print("O valor de saque ultrapassa o limite máximo de R$500.00.")
                else:
                    print("Limite máximo de saque atingido.")
            else:
                print("Saldo insuficiente.")
        else:
            print("Valor insrido inválido. O valor do saque deve ser maior que 0.")

    def extract(self):
        print("\n---- EXTRATO ----")
        print(f"Saldo: R${self.balance:.2f}")
        print(f"Número de depósitos realizados: {self.deposit_count}")
        print(f"Número de saques realizados: {self.withdrawal_count}")

def display_menu():
    print("\n---- Banco DIO ----")
    print("1. Depósito")
    print("2. Saque")
    print("3. Extrato")
    print("4. Sair")


system_bank = BankAccount()

while True:
    display_menu()
    choice = input("Digite a opção desejada (1-4): ")

    if choice == "1":
        system_bank.deposit()
    elif choice == "2":
        system_bank.withdraw()
    elif choice == "3":
        system_bank.extract()
    elif choice == "4":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida. Tente uma opção entre 1 e 4.")


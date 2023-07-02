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

class User:
    def __init__(self, name, date_of_birth, cpf, address):
        self.name = name
        self.date_of_birth = date_of_birth
        self.cpf = cpf
        self.address = address


class Account:
    account_number_sequence = 1

    def __init__(self, user):
        self.agency = "0001"
        self.account_number = Account.account_number_sequence
        self.user = user
        Account.account_number_sequence += 1

class Bank:
    def __init__(self):
        self.customers = []
        self.accounts = []

    def register_user(self, name, date_of_birth, cpf, address):
        if self.get_customer_by_cpf(cpf) is None:
            user = User(name, date_of_birth, cpf, address)
            self.customers.append(user)
            print(f"Usuário {user.name} registrado com sucesso.")
        else:
            print("Já existe um usuário cadastrado com esse CPF.")

    def register_account(self, user):
        account = Account(user)
        self.accounts.append(account)
        print(f"Conta {account.account_number} criada para o usuário {user.name}.")

    def get_customer_by_cpf(self, cpf):
        for customer in self.customers:
            if customer.cpf == cpf:
                return customer
        return None

    def list_registered_users(self):
        print("\nUsuários registrados:")
        for user in self.customers:
            print(f"Nome: {user.name}, CPF: {user.cpf}")

    def list_user_accounts(self, cpf):
        user = self.get_customer_by_cpf(cpf)
        if user:
            print(f"\nContas vinculadas ao usuário {user.name} (CPF: {user.cpf}):")
            for account in self.accounts:
                if account.user == user:
                    print(f"Número da conta: {account.account_number}")
        else:
            print("Usuário não encontrado.")

def display_menu():
    print("\n---- Bank DIO ----")
    print("1. Registrar Usuário")
    print("2. Registrar conta bancária")
    print("3. Depósito")
    print("4. Saque")
    print("5. Extrato")
    print("6. Listar usuários registrados")
    print("7. Listar contas dos usuários")
    print("8. Sair")


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


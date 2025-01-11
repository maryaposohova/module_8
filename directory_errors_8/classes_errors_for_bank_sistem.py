# Банковская система управления счетами, и управление ошибками
class InsufficientFundsError(Exception):
    """Исключение для обработки недостатка средств на счете."""

    def __init__(self, message='Недостаточно средств на счете для выполнения операции.'):
        self.message = message
        super().__init__(self.message)


class AccauntNotFoundError(Exception):
    """Исключение для обработки случая, когда счет не найден."""

    def __init__(self, message='Счет не найден. Проверьте номер счета и попробуйте снова.'):
        self.message = message
        super().__init__(self.message)


class InvalidAmountError(Exception):
    """Исключение для обработки случая, когда введена неверная сумма."""

    def __init__(self, message='Введена неверная сумма Сумма должна быть положительным числом.'):
        self.message = message
        super().__init__(self.message)


class BankAccount:
    """Класс для представления банковского счета."""

    def __init__(self, account_number, owner, balance=0.0):
        self.account_number = account_number
        self.owher = owner
        self.balance = balance

    def deposit(self, amount):
        if amount <= 0:  # если депозит меньше или равен 0
            raise InvalidAmountError('Сумма депозита должна быть положительным числом.')
        self.balance += amount
        print(f'Депозит успешно выполнен. Текущий баланс {self.balance: .2f}')

    def withdraw(self, amount):
        if amount <= 0:  # если сумма снятия меньше или равна 0
            raise InvalidAmountError('Сумма снятия должна быть положительным числом.')
        if self.balance < amount:  # если баланс меньше суммы снятия
            raise InsufficientFundsError('Недостаточно средств на счете для выполнения операции.')
        self.balance -= amount
        print(f'Снятие успешно выполнено. Текущий баланс {self.balance: .2f}')

    def get_balance(self):
        return self.balance


class Bank:
    """Класс для управления несколькими банковскими счетами"""

    def __init__(self):
        self.accounts = {}  # инициализация аккаунтов? для хранения счетов

    def create_account(self, account_number, owner, initial_balance=0.0):
        if account_number in self.accounts:  # если данный аккаунт есть в словаре с аккаунтами
            raise ValueError("Счет с таким номером уже существует.")
        new_account = BankAccount(account_number, owner, initial_balance)
        self.accounts[account_number] = new_account
        print(f"Счет успешно создан для {owner} с номером {account_number} и начальным балансом {initial_balance}")

    def get_account(self, account_number):
        if account_number not in self.accounts:  # если данного аккаунта нет в словаре с аккаунтами
            raise AccauntNotFoundError("Счет с таким номером не найден.")
        return self.accounts[account_number]

    # def deposit_to_account(self, account_number, amount):
    #     account = self.get_account(account_number)
    #     account.deposit(amount)
    #
    # def withdraw_from_account(self, account_number, amount):
    #     account = self.get_account(account_number)
    #     account.withdraw(amount)

    def deposit_to_account(self, account_number, amount):
        account1 = self.get_account(account_number)
        account1.deposit(amount)

    def withdraw_from_account(self, account_number, amount):
        account1 = self.get_account(account_number)
        account1.withdraw(amount)


# Пример использования системы банка
print('# Пример использования системы банка')
bank = Bank()
# Создание счетов
try:
    bank.create_account("12345", 'Иван Иванов', 1000)
    bank.create_account("06789", 'Юргис Иванаускас', 500)
except ValueError as ve:
    print(ve)

print()

# Пополнение счета
print('# Пополнение счета')
try:
    bank.deposit_to_account('12345', 200)
    bank.deposit_to_account('12345', 20000)
except (AccauntNotFoundError, InvalidAmountError) as e:
    print(e)

print()

# Снятие средств
print('# Снятие средств')
try:
    bank.withdraw_from_account('12345', 5)
    bank.withdraw_from_account('12345', 220330)
except (AccauntNotFoundError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)

print()

# Проверка баланса
print('# Проверка баланса')
try:
    account = bank.get_account('12345')
    print(f'баланс счетаЖ {account.account_number}: {account.get_balance(): .2f}')
except AccauntNotFoundError as e:
    print(e)

print()

# Попытка снять деньги с несуществующего счета
print('# Попытка снять деньги с несуществующего счета')
try:
    bank.withdraw_from_account('12345', 50)
    bank.withdraw_from_account('1', 50)
except (AccauntNotFoundError, InvalidAmountError, InsufficientFundsError) as e:
    print(e)

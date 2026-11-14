class ATM:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print(f"Ваш баланс {self.balance} рублей")

    def deposit(self, amount):
        if amount > 49:
            self.balance = self.balance + amount
            print(f"Вы внесли {amount} Ваш баланс {self.balance}")
        else:
            print(f"Сумма должна быть от 50 руб")

    def withdraw(self, amount):
        if amount > 50 and amount <= self.balance:
            self.balance = self.balance - amount
            print(f"Вы сняли {amount} руб. Ваш баланс {self.balance} руб")
        else:
            print(f"Сумма должна быть от 50 рублей или недостаточно средств")

    def perevod(self, amount):
        USD = roumd(self.balance / 80, 1)
        EUR = round(self.balance / 93, 1)
        print(f"Баланс в долларах (USD)_{USD}")
        print(f"Баланс в евро (EUR) {EUR}")


class SecureATM(ATM):
    def __init__(self, balance, pin):
        super().__init__(balance)
        self.pin = pin
        self.is_autentificated = False

    def autentificated(self, enter_pin):
        if enter_pin == self.pin:
            self.is_autentificated = True
            print(f"Аунтефикация прошла успешна!")
        else:
            print(f"Неправильный Pin-code")

    def check_balance(self):
        if self.is_autentificated == True:
            super().check_balance()
        else:
            print(f"Необхдимо пройти аунтефикацию")

    def withdraw(self, amount):
        if self.is_autentificated == True:
            super().withdraw(amount)
        else:
            print(f"Необхдимо пройти аунтефикацию")

    def deposit(self, amount):
        if self.is_autentificated == True:
            super().deposit(amount)
        else:
            print(f"Необхдимо пройти аунтефикацию")

    def perevod(self):
        if self.is_autentificated == True:
            super().perevod()
        else:
            print(f"Необходимо пройти аунтефикацию")

def atm_menu(atm):
    while True:
        print("\nМеню банкомата")
        print("1. Проверить баланс")
        print("2. Внести деньги")
        print("3. Снять деньги")
        print("4. Пройти аутенфикацию")
        print("5. Посмотреть баланс в EUR и USD: ")
        print("6. Выход")
        choice = input("Выберети действие: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            summa = int(input("Введите сумму для пополнения:"))
            atm.deposit(summa)
        elif choice == "3":
            summa = int(input("Введите сумму для снятия:"))
            atm.withdraw(summa)
        elif choice == "4":
            enter_pin = int(input("Введите Pin-code для входа:"))
            atm.autentificated(enter_pin)
        elif choice == "5":
            atm.perevod()
        elif choice == "6":
            print("До свидания")
            break
        else:
            print("Неправильный ввод")

pin = int(input("Установите Pin-code: "))
secure_atm = SecureATM(10000, pin)

enter_pin = int(input("Введите Pin-code для входа:"))
secure_atm.autentificated(enter_pin)

atm_menu(secure_atm)

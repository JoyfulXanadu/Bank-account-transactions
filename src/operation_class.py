from _datetime import datetime


class Operation:
    """Класс Операция"""

    def __init__(self, operation):
        """Инициализация объекта операции
        :param operation: словарь с данными по операции
        """
        self.operation = operation

    def __repr__(self):
        """Метод для представления объекта операции в виде строки"""
        return f"Class Operation({self.operation})"

    def get_date(self):
        """Метод для получения даты операции
        :return: строка с датой в формате 'дд.мм.гггг'
        """
        operation_date_str = self.operation["date"]
        operation_date = datetime.strptime(operation_date_str, "%Y-%m-%dT%H:%M:%S.%f")
        return operation_date.strftime("%d.%m.%Y")

    def get_description(self):
        """Метод для получения описания операции
        :return: строка с описанием операции
        """
        return self.operation["description"]

    def get_account_from(self):
        """Метод для получения данных счета/карты отправления, если они есть
        :return: строка с данными счета/карты отправления или пустая строка
        """
        if "from" in self.operation.keys():
            return self.operation["from"]
        else:
            return ""

    def get_account_to(self):
        """Метод для получения данных счета/карты назначения
        :return: строка с данными счета/карты назначения
        """
        return self.operation["to"]

    def hide_number(self, account):

        """Метод для скрытия части номера счета/карты
        :param account: строка с данными счета/карты
        :return: строка с скрытым номером счета/карты
        """

        if account == "":
            return "Внесение средств"
        else:
            account = account.split(" ")
            account_number = account[-1]
            account.pop(len(account) - 1)
            account_name = " ".join(account)
        if "Счет" in account:
            return f"{account_name} **{account_number[12:16]}"
        else:
            return f"{account_name} {account_number[0:4]} {account_number[5:7]}** **** {account_number[12:16]}"

    def get_amount(self):
        """Метод для получения суммы операции и валюты
    :return: строка с суммой и валютой операции
    """
        return f'{self.operation["operationAmount"]["amount"]} {self.operation["operationAmount"]["currency"]["name"]}'

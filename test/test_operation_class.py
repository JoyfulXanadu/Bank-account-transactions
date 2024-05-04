import unittest
from datetime import datetime
from src.operation_class import Operation


class TestOperationMethods(unittest.TestCase):

    def setUp(self):
        # Создаем объект операции для тестирования
        self.operation_data = {
            "date": "2022-01-01T12:00:00.000",
            "description": "Payment",
            "from": "Account 1234567890123456",
            "to": "Card 9876543210987654",
            "operationAmount": {
                "amount": 100.00,
                "currency": {"name": "USD"}
            }
        }
        self.operation = Operation()
        self.operation.init(self.operation_data)

    def test_get_date(self):
        """Тест метода get_date на корректное извлечение и форматирование даты"""
        expected_date = datetime.strptime("2022-01-01T12:00:00.000", "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")
        self.assertEqual(self.operation.get_date(), expected_date)

    def test_get_description(self):
        """Тест метода get_description на корректное получение описания операции"""
        self.assertEqual(self.operation.get_description(), "Payment")

    def test_get_account_from(self):
        """Тест метода get_account_from на корректное получение данных о счете/карте отправления"""
        self.assertEqual(self.operation.get_account_from(), "Account 1234567890123456")

    def test_get_account_to(self):
        """Тест метода get_account_to на корректное получение данных о счете/карте назначения"""
        self.assertEqual(self.operation.get_account_to(), "Card 9876543210987654")

    def test_hide_number(self):
        """Тест метода hide_number на корректное скрытие части номера счета/карты"""
        self.assertEqual(self.operation.hide_number("Account 1234567890123456"), "Account 1234 56** **** 3456")
        self.assertEqual(self.operation.hide_number("Card 9876543210987654"), "Card 9876 54** **** 7654")
        self.assertEqual(self.operation.hide_number(""), "Внесение средств")

    def test_get_amount(self):
        """Тест метода get_amount на корректное получение суммы операции и валюты"""
        self.assertEqual(self.operation.get_amount(), "100.0 USD")


if __name__ == '__main__':
    unittest.main()

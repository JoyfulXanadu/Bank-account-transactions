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
        self.operation = Operation(self.operation_data)

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
        hidden_account_from = self.operation.hide_number(self.operation_data["from"])
        hidden_account_to = self.operation.hide_number(self.operation_data["to"])
        self.assertEqual(hidden_account_from, "Account 1234 67** **** 3456")
        self.assertEqual(hidden_account_to, "Card 9876 43** **** 7654")



    def test_get_amount(self):
        """Тест метода get_amount на корректное получение суммы операции и валюты"""
        self.assertEqual(self.operation.get_amount(), "100.0 USD")

if __name__ == 'main':
    unittest.main()

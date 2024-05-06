import unittest
from unittest.mock import mock_open, patch
from src.utils import load_operations, get_last_five_operations


class TestOperationsFunctions(unittest.TestCase):

    @patch('builtins.open', new_callable=mock_open, read_data='[{"id": 1, "state": "EXECUTED", "date": "2022-01-01"},'
                                                            '{"id": 2, "state": "PENDING", "date": "2022-01-02"},'
                                                            '{"id": 3, "state": "EXECUTED", "date": "2022-01-03"}]')
    def test_load_operations(self, mock_file):
        """Тест функции load_operations на правильную загрузку данных из файла"""
        operations_list = load_operations()
        self.assertEqual(len(operations_list), 3)

    def test_get_last_five_operations(self):
        """Тест функции get_last_five_operations на выбор пяти последних операций"""
        operations_list = [{"id": 1, "state": "EXECUTED", "date": "2022-01-01"},
                           {"id": 2, "state": "PENDING", "date": "2022-01-02"},
                           {"id": 3, "state": "EXECUTED", "date": "2022-01-03"}]
        last_five_operations = get_last_five_operations(operations_list)
        self.assertEqual(len(last_five_operations), 2)


if __name__ == '__main__':
    unittest.main()

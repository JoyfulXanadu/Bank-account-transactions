# Импортируем необходимые библиотеки
import json
import os

# Определяем путь к файлу данных и к файлу операций
path_to_data = os.path.abspath("../data/")
path_to_operations = os.path.join(path_to_data, "operations.json")

def load_operations():
    """Загружает данные из файла и формирует список всех операций клиента """
    with open(path_to_operations, "r", encoding='utf8') as file:
        operations_list = json.load(file)
    return operations_list

def get_last_five_operations(operations_list):
    """Составляет отсортированный по дате список из 5 последних выполненных клиентом операций
    (без пустых и отклоненных операции)"""
    operations_list_clean = [opr for opr in operations_list if opr and opr.get("state") == "EXECUTED"]
    operations_list_clean.sort(key=lambda dictionary: dictionary.get("date", 0), reverse=True)
    last_five_operations = operations_list_clean[:5]
    return last_five_operations

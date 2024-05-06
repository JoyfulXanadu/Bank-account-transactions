# Импортируем необходимые функции и классы
from src.utils import load_operations, get_last_five_operations
from src.operation_class import Operation

# Загружаем список всех операций клиента
operations_list = load_operations()

# Создаем список из 5 последних выполненных (EXECUTED) клиентом операций
last_five_operations = get_last_five_operations(operations_list)

# Перебираем список и для каждой операции выводим данные в соответствии с требованиями
for element in last_five_operations:
    operation = Operation(element)
    print(f"""\n{operation.get_date()} {operation.get_description()}
{operation.hide_number(operation.get_account_from())} -> {operation.hide_number(operation.get_account_to())}
{operation.get_amount()}""")

from typing import TypedDict
from httpx import Response, Client

# Используем абсолютный импорт или try/except для обработки обоих случаев
try:
    # Для случая когда файл импортируется как модуль
    from ...clients.api_client import APIClient
except ImportError:
    # Для случая когда файл запускается напрямую
    import sys
    import os
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    from clients.api_client import APIClient


class CreateUserRequest(TypedDict):
    """
    Типизированный словарь для запроса создания пользователя.
    
    Attributes:
        email: Email пользователя
        password: Пароль пользователя
        lastName: Фамилия пользователя
        firstName: Имя пользователя
        middleName: Отчество пользователя (опционально)
    """
    email: str
    password: str
    lastName: str
    firstName: str
    middleName: str | None


class PublicUsersClient(APIClient):
    """
    API клиент для работы с публичными эндпоинтами пользователей.
    Предоставляет методы для взаимодействия с API пользователей
    без необходимости аутентификации.
    """
    
    def create_user_api(self, request: CreateUserRequest) -> Response:
        """
        Создает нового пользователя через POST запрос к эндпоинту /api/v1/users.
        
        Метод выполняет запрос на создание пользователя с предоставленными данными.
        Эндпоинт не требует аутентификации и доступен публично.
        
        Args:
            request: Словарь с данными для создания пользователя, содержащий:
                - email (str): Email пользователя
                - password (str): Пароль пользователя
                - lastName (str): Фамилия пользователя
                - firstName (str): Имя пользователя
                - middleName (str | None): Отчество пользователя (может быть None)
        
        Returns:
            Response: Объект ответа httpx.Response с данными созданного пользователя
            и статус-кодом ответа сервера.
        """
        return self.post("/api/v1/users", json=request)


# Проверочный код (выполняется только при прямом запуске файла)
if __name__ == "__main__":
    # Тестирование клиента
    import sys
    import os
    
    # Добавляем путь для корректного импорта
    sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
    
    # Создаем клиент
    base_url = "http://localhost:8000"  # Замените на ваш URL
    client = PublicUsersClient(Client(base_url=base_url, timeout=30.0))
    
    # Тестовые данные
    test_data: CreateUserRequest = {
        "email": f"test2.user.{os.getpid()}@example.com",
        "password": "test_password_123",
        "lastName": "Testov",
        "firstName": "Test",
        "middleName": "Testovich"
    }
    print("Testing PublicUsersClient...")
    print(f"Request data: {test_data}")
    
    try:
        # Выполняем запрос
        response = client.create_user_api(test_data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text}")
        if response.status_code == 201:
            print("✅ User created successfully!")
        else:
            print("❌ Failed to create user")   
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure the server is running on", base_url)
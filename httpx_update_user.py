import httpx
import time


def get_random_email() -> str:
    return f"test.{time.time()}@example.com"

# Создаем пользователя 
create_user_payload = {
    "email": get_random_email(),
    "password": "string",
    "lastName": "string",
    "firstName": "string",
    "middleName": "string"
}

create_user_response = httpx.post(
    "http://localhost:8000/api/v1/users", 
    json=create_user_payload
)

assert create_user_response.status_code == 200, \
            'ОШИБКА!!! Проблема с запросом создания пользователя.'
            
create_user_response_data = create_user_response.json()
print('Create user data:', create_user_response_data)
print()

# Проходим аутентификацию 
login_payload = {
    "email": create_user_payload['email'],
    "password": create_user_payload['password']
}

login_response = httpx.post(
    "http://localhost:8000/api/v1/authentication/login", 
    json=login_payload
)

assert login_response.status_code == 200, \
            'ОШИБКА!!! Проблема с запросом аутентификации.'
            
login_response_data = login_response.json()
print('Login data:', login_response_data)
print()


# Получаем токен авторизации из ответа
auth_token = login_response_data['token']['accessToken']
print(f'Токен успешно получен')
print()

# Получаем user_id из ответа создания пользователя
user_id = create_user_response_data['user']['id']
print(f'User ID: {user_id}')

# Обновляем пользователя с помощью PATCH запроса
update_user_payload = {
    "email": get_random_email(),  # Новый случайный email
    "lastName": "UpdatedLastName",
    "firstName": "UpdatedFirstName",
    "middleName": "UpdatedMiddleName"
}

# Добавляем заголовок авторизации
headers = {
    "Authorization": f"Bearer {auth_token}",
    "Content-Type": "application/json"
}

# Выполняем PATCH запрос для обновления пользователя
update_user_response = httpx.patch(
    f"http://localhost:8000/api/v1/users/{user_id}",
    json=update_user_payload,
    headers=headers
)
assert login_response.status_code == 200, \
            'ОШИБКА!!! Проблема с запросом обновления пользователя.'
            
print('Update user response:', update_user_response.json())
print(f'Status code: {update_user_response.status_code}')
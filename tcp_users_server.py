import socket  # Импортируем модуль socket для работы с сетевыми соединениями


def server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_address = ('localhost', 12345)
    server_socket.bind(server_address)
    server_socket.listen(10)  # Поддерживаем до 10 подключений в очереди
    print("Сервер запущен и ждет подключений...")
    list_messages = []  # список всех сообщений

    while True:
        # Ожидаем и принимаем новое подключение
        client_socket, client_address = server_socket.accept()
        print(f"Пользователь с адресом: {client_address} подключился к серверу")
        
        try:
            # Получаем данные от клиента
            data = client_socket.recv(1024).decode()
            if data:
                result = f"Пользователь с адресом: {client_address} отправил сообщение: {data}"
                print(result)
                list_messages.append(result)
                
                # Отправляем всю историю сообщений клиенту
                client_socket.send('\n'.join(list_messages).encode())
        
        except Exception as e:
            print(f"Ошибка при работе с клиентом {client_address}: {e}")
        finally:
            # Закрываем соединение с текущим клиентом
            client_socket.close()


if __name__ == '__main__':
    server()

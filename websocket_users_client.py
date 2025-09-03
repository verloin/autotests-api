import asyncio

import websockets


async def client():
    uri = "ws://localhost:8765"  # Адрес сервера
    
    try:
        async with websockets.connect(uri) as websocket:
            message = "Привет, сервер!"  # Сообщение, которое отправит клиент
            await websocket.send(message)  # Отправляем сообщение

            for _ in range(5):
                message = await websocket.recv()
                print(message)
    except websockets.exceptions.ConnectionClosed:
        print("Соединение было закрыто сервером")
    except ConnectionRefusedError:
        print("Не удалось подключиться к серверу. Убедитесь, что сервер запущен.")
    except Exception as e:
        print(f"Произошла ошибка: {e}")


asyncio.run(client())

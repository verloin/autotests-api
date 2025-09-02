import grpc
from concurrent import futures
import course_service_pb2
import course_service_pb2_grpc

# Создаем класс-обработчик, который наследуется от сгенерированного класса сервиса
class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    
    # Реализуем метод GetCourse, который был описан в .proto файле
    def GetCourse(self, request, context):
        # Логируем полученный запрос (опционально)
        print(f"Received request for course_id: {request.course_id}")
        
        # Создаем ответ, используя сгенерированный класс GetCourseResponse
        response = course_service_pb2.GetCourseResponse(
            course_id=request.course_id,  # Берем course_id из запроса
            title="Автотесты API",  # Статическое название
            description="Будем изучать написание API автотестов"  # Статическое описание
        )
        return response

def serve():
    # Создаем сервер с пулом потоков
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    
    # Добавляем наш сервис на сервер
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(
        CourseServiceServicer(), server
    )
    
    # Настраиваем порт прослушивания
    server.add_insecure_port('[::]:50051')
    
    # Запускаем сервер
    server.start()
    print("Server started on port 50051")
    
    # Ожидаем завершения работы сервера
    try:
        server.wait_for_termination()
    except KeyboardInterrupt:
        server.stop(0)
        print("Server stopped")

# Точка входа в приложение
if __name__ == '__main__':
    serve()
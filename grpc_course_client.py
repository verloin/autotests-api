import grpc
import course_service_pb2
import course_service_pb2_grpc

def run():
    # Устанавливаем соединение с сервером на localhost:50051
    with grpc.insecure_channel('localhost:50051') as channel:
        # Создаем клиентский stub (заглушку) для взаимодействия с сервером
        stub = course_service_pb2_grpc.CourseServiceStub(channel)
        
        # Создаем запрос с course_id = "api-course"
        request = course_service_pb2.GetCourseRequest(course_id="api-course")
        
        # Вызываем удаленный метод GetCourse и получаем ответ
        response = stub.GetCourse(request)
        
        # Выводим полученный ответ в консоль
        print("Response from server:")
        print(response)

# Точка входа в приложение
if __name__ == '__main__':
    run()
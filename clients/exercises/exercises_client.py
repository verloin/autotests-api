from typing import TypedDict

from httpx import Response

from clients.api_client import APIClient


class CreateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на создание задания.
    """
    title: str | None
    courseId: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None
    
    
class UpdateExercisesRequestDict(TypedDict):
    """
    Описание структуры запроса на обновление задания.
    """
    title: str | None
    maxScore: int | None
    minScore: int | None
    orderIndex: int | None
    description: str | None
    estimatedTime: str | None


class ExercisesClient(APIClient):
    """
    Клиент для работы с /api/v1/exercises
    """

    def get_exercises_api(self) -> Response:
        """
        Метод получения списка заданий.

        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get("/api/v1/exercises")

    def get_exercise_api(self, exercise_id: str) -> Response:
        """
        Метод получения списка заданий по идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.get(f"/api/v1/exercises/{exercise_id}")
    
    def create_exercise_api(self, request: CreateExercisesRequestDict) -> Response:
        """
        Метод создания задания.

        :param request: Словарь с данными.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises", json=request)

    def update_user_api(self, exercise_id: str, request: UpdateExercisesRequestDict) -> Response:
        """
        Метод обновления задания по идентификатору.

        :param exercise_id: Идентификатор задания.
        :param request: Словарь с данными.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.patch(f"/api/v1/exercises/{exercise_id}", json=request)

    def delete_user_api(self, exercise_id: str) -> Response:
        """
        Метод удаления задания по идентификатору.

        :param exercise_id: Идентификатор задания.
        :return: Ответ от сервера в виде объекта httpx.Response
        """
        return self.delete(f"/api/v1/exercises/{exercise_id}")

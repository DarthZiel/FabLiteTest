from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import CustomUser


class AccountTests(APITestCase):

    def setUp(self):
        users_data = [
            {"email": "user1@mail.ru", "first_name": "Иван", "last_name": "Иванов", "password": "qaws1234"},
            {"email": "user2@mail.ru", "first_name": "Пётр", "last_name": "Петров", "password": "qaws1234"},
            {"email": "user3@mail.ru", "first_name": "Мария", "last_name": "Сидорова", "password": "qaws1234"},
            {"email": "user11@mail.ru", "first_name": "София", "last_name": "Николаева", "password": "qaws1234"},
            {"email": "user12@mail.ru", "first_name": "Анна", "last_name": "Кузнецова", "password": "qaws1234"},
            {"email": "user13@mail.ru", "first_name": "Дмитрий", "last_name": "Смирнов", "password": "qaws1234"},
            {"email": "user14@mail.ru", "first_name": "Елена", "last_name": "Морозова", "password": "qaws1234"},
            {"email": "user15@mail.ru", "first_name": "Алексей", "last_name": "Петухов", "password": "qaws1234"},
            {"email": "user16@mail.ru", "first_name": "Ольга", "last_name": "Васильева", "password": "qaws1234"},
            {"email": "user17@mail.ru", "first_name": "Максим", "last_name": "Алексеев", "password": "qaws1234"},
            {"email": "user18@mail.ru", "first_name": "Татьяна", "last_name": "Зайцева", "password": "qaws1234"},
        ]

        # Создание пользователей в цикле
        for user_data in users_data:
            CustomUser.objects.create(
                email=user_data['email'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                password=user_data['password']
            )

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('registration')
        data = {"email": "test@mail.ru", "first_name": "Уолтер", "last_name": "Вайт", "password": "qaws1234"}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        user = CustomUser.objects.get(email='test@mail.ru')
        self.assertEqual(user.email, 'test@mail.ru')

    def test_user_list(self):
        url = reverse('user-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 10)

    def test_update_account(self):
        user = CustomUser.objects.get(email='user2@mail.ru')
        url = reverse('user', kwargs={'pk': user.pk})
        data = {"email": "updated_user2@mail.ru", "first_name": "Сергей", "last_name": "Бурунов", "password": "new1234pass"}

        # Отправляем запрос на обновление данных пользователя
        response = self.client.put(url, data, format='json')

        # Проверяем, что запрос вернул ожидаемый HTTP статус код
        self.assertIn(response.status_code, [status.HTTP_200_OK, status.HTTP_201_CREATED])

        # Если код статуса 200 OK, проверяем обновленные данные пользователя
        if response.status_code == status.HTTP_200_OK:
            updated_user = CustomUser.objects.get(pk=user.pk)
            self.assertEqual(updated_user.email, "updated_user2@mail.ru")
            self.assertEqual(updated_user.first_name, "Сергей")
            self.assertEqual(updated_user.last_name, "Бурунов")

    def test_partial_update_account(self):
        user = CustomUser.objects.get(email='user1@mail.ru')
        url = reverse('user', kwargs={'pk': user.pk})
        data = {"first_name": "Сергей"}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        updated_user = CustomUser.objects.get(pk=user.pk)
        self.assertEqual(updated_user.first_name, "Сергей")

    def test_delete_account(self):
        user = CustomUser.objects.get(email='user3@mail.ru')
        url = reverse('user', kwargs={'pk': user.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(CustomUser.DoesNotExist):
            CustomUser.objects.get(pk=user.pk)

    def test_user_authentication(self):
        url = reverse('user')
        self.client.login(email='testuser@mail.ru', password='qaws1234')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


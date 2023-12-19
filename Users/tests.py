
# from django.test import TestCase
# from rest_framework.test import APIClient
# from django.contrib.auth.models import User
# from rest_framework import status

# class SocialAuthViewsTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', password='test')

#     # def test_google_login_view(self):
#     #     response = self.client.post('dj-rest-auth/google/')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # def test_facebook_connect_view(self):
#     #     response = self.client.post('/accounts/facebook/connect/')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

#     # def test_twitter_connect_view(self):
#     #     response = self.client.post('/accounts/twitter/connect/')
#     #     self.assertEqual(response.status_code, status.HTTP_200_OK)

# class UserViewsTest(TestCase):
#     def setUp(self):
#         self.client = APIClient()
#         self.user = User.objects.create_user(username='testuser', password='test')

#     def test_user_list_view_authenticated(self):
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get('/users/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_list_view_unauthenticated(self):
#         response = self.client.get('/users/')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_user_detail_view_authenticated(self):
#         self.client.force_authenticate(user=self.user)
#         response = self.client.get(f'/users/{self.user.id}/')
#         self.assertEqual(response.status_code, status.HTTP_200_OK)

#     def test_user_detail_view_unauthenticated(self):
#         response = self.client.get(f'/users/{self.user.id}/')
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

#     def test_user_creation_view_authenticated(self):
#         self.client.force_authenticate(user=self.user)
#         data = {'username': 'newuser', 'password': 'newpassword'}
#         response = self.client.post('/users/', data)
#         self.assertEqual(response.status_code, status.HTTP_201_CREATED)

#     def test_user_creation_view_unauthenticated(self):
#         data = {'username': 'newuser', 'password': 'newpassword'}
#         response = self.client.post('/users/', data)
#         self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)



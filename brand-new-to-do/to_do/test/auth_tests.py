"""User create and login tests"""
import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status


class UserTestCase(TestCase):
    fixtures = ['users.json', 'dashboards.json', 'goals.json']

    def setUp(self):
        """Setting data for test."""

        self.client = APIClient()

    def test_12_create_user(self):
        """ Test User auth. User Create with correct data"""
        post_data = {
            "username": "TestCaseUser",
            "email": "test_case@test.com",
            "password": "Test1234",
            }

        response = self.client.post('/auth/create/', data=json.dumps(post_data),
                                content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_13_create_user(self):
        """ Test User auth. User Create with incorrect data"""
        post_data = {
            "username": "TestCaseUser",
            "email": "test_case@test",
            "password": "Test1234",
            }
        expected_result = {"email": ["Enter a valid email address."]}

        response = self.client.post('/auth/create/', data=json.dumps(post_data),
                                content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(expected_result, response.data)

    def test_14_login_user(self):
        """ Test User auth. User Login with correct data"""
        post_data = {
            "username": "TestUser",
            "password": "E@z@8T7h5sU@vKc",
            }

        response = self.client.post('/auth/login/', data=json.dumps(post_data),
                                content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_15_login_user(self):
        """ Test User auth. User Login with incorrect data"""
        post_data = {
            "username": "TestUser",
            "password": "Test1234",
            }

        response = self.client.post('/auth/login/', data=json.dumps(post_data),
                                content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

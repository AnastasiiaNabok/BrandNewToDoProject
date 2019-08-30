"""Goal create, update and retrieve  tests"""
import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status


class GoalTestCase(TestCase):
    fixtures = ['users.json', 'dashboards.json', 'goals.json']

    def setUp(self):
        """Setting data for test."""

        self.user, _ = User.objects.get_or_create(email='test@gmail.com')
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + token.key)

    def test_1_post_goal(self):
        """Test Goal create with correct data"""
        post_data = {
            "user": self.user.id,
            "dashboard": 1,
            "title": "test_1",
            "is_urgent": True,
            "is_important": True,
            "status": True
            }

        resp = self.client.post('/api/goals/', data=json.dumps(post_data),
                                content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(17, resp.data.get('id'))

    def test_2_post_goal(self):
        """Test Goal create with not full data"""
        post_data = {
            "title": "test_1",
            "is_urgent": True,
            "is_important": True,
            "status": True
        }

        response = self.client.post('/api/goals/', data=json.dumps(post_data), content_type='application/json')
        expected_result = {'dashboard': ['This field is required.']}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(expected_result, response.data)

    def test_3_get_goals(self):
        """Test method get for Goals"""
        response = self.client.get('/api/goals/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(10, len(response.data))

    def test_4_update_goal(self):
        """Test Goal update with correct data"""
        post_data = {
            "title": "updated title",
            "status": False
        }
        resp = self.client.put('/api/goal/16/', data=json.dumps(post_data), content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertEqual("updated title", resp.data.get('title'))

    def test_5_update_goal(self):
        """Test Goal update with correct data"""
        post_data = {
            "dashboard": 2,
        }
        resp = self.client.put('/api/goal/16/', data=json.dumps(post_data), content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

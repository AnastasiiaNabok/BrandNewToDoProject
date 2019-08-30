"""Dashboard create and retrieve tests"""
import json

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework import status


class DashboardTestCase(TestCase):
    fixtures = ['users.json', 'dashboards.json', 'goals.json']

    def setUp(self):
        """Setting data for test."""

        self.user, _ = User.objects.get_or_create(email='test@gmail.com')
        token, _ = Token.objects.get_or_create(user=self.user)
        self.client = APIClient()
        self.client.credentials(
            HTTP_AUTHORIZATION='Token ' + token.key)

    def test_6_post_dashboard(self):
        """Test Dashboard create with correct data"""
        post_data = {
            "user": self.user.id,
            "name": "test dashboard",
            }

        resp = self.client.post('/api/dashboards/', data=json.dumps(post_data),
                                content_type='application/json')
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        self.assertEqual(2, resp.data.get('id'))

    def test_7_post_dashboard(self):
        """Test Dashboard create with not full data"""
        post_data = {
            "user": self.user.id,
        }

        response = self.client.post('/api/dashboards/', data=json.dumps(post_data),
                                content_type='application/json')
        expected_result = {'name': ['This field is required.']}
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertDictEqual(expected_result, response.data)

    def test_8_get_dashboards(self):
        """Test method get for Goals"""
        response = self.client.get('/api/dashboards/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))

    def test_9_get_dashboards_by_user(self):
        """Test get Dashboard by user """
        response = self.client.get('/api/dashboards/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(1, len(response.data))

    def test_10_get_dashboard_by_id(self):
        """Test get Dashboard by id """
        response = self.client.get('/api/dashboard/1/', content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_11_get_dashboard_by_id(self):
        """Test get Dashboard by id, when id doesn't exist"""
        response = self.client.get('/api/dashboard/3/', content_type='application/json')
        expected_result = {"detail": "Not found."}
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertDictEqual(expected_result, response.data)


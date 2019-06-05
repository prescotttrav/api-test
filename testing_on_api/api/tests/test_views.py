import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import API
from ..serializers import APISerializer

# intialize the Client app for the API
client = Client()

class GetAllAPITest(TestCase):
    ''' Test module for GET all in API '''

    def setUp(self):
        API.objects.create(
            name='John Smith', age=36, position='engineer', company='Engineering Consultants')
        API.objects.create(
            name='Jordan Stevens', age=42, position='program manager', company='San Diego Group')
        API.objects.create(
            name='Jim Whilmer', age=22, position='accountant', company='Bank Company')
        API.objects.create(
            name='James Snow', age=16, position='waiter', company='Good Food Co')

        def test_get_all(self):
            response = client.get(reverse('get_post_api'))
            api_data = API.object.all()
            serializer = APISerializer(api_data, many=True)
            self.assertEqual(response.data, serializer.data)
            self.assertEqual(response.status_code, status.HTTP_200_OK)

class GetSingleAPITest(TestCase):
    ''' Test module for GET single in API '''

    def setUp(self):
        self.john = API.objects.create(
            name='John Smith', age=36, position='engineer', company='Engineering Consultants')
        self.jordan = API.objects.create(
            name='Jordan Stevens', age=42, position='program manager', company='San Diego Group')
        self.jim = API.objects.create(
            name='Jim Whilmer', age=22, position='accountant', company='Bank Company')
        self.james = API.objects.create(
            name='James Snow', age=16, position='waiter', company='Good Food Co')

    def test_get_valid_single(self):
        response = client.get(
            reverse('get_delete_update_api', kwargs={'pk': self.jim.pk}))
        api_data = API.objects.get(pk=self.jim.pk)
        serializer = APISerializer(api_data)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single(self):
        response = client.get(
            reverse('get_delete_update_api', kwargs={'pk': 16}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class CreateNewTest(TestCase):
    ''' Test module for inserting new to api '''

    def setUp(self):
        self.valid_payload = {
            'name': 'John Smith',
            'age': 36,
            'position': 'engineer',
            'company': 'Engineering Consultants'
        }
        self.invalid_payload = {
            'name': '',
            'age': 36,
            'position': 'engineer',
            'company': 'Engineering Consultants'
        }

    def test_create_valid(self):
        response = client.post(
            reverse('get_post_api'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid(self):
        response = client.post(
            reverse('get_post_api'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class UpdateSingleTest(TestCase):
    ''' Test module for updating an existing record '''

    def setUp(self):
        self.john = API.objects.create(
            name='John Smith', age=36, position='engineer', company='Engineering Consultants')
        self.jordan = API.objects.create(
            name='Jordan Stevens', age=42, position='program manager', company='San Diego Group')
        self.valid_payload = {
            'name': 'John Smith',
            'age': 39,
            'position': 'sr. engineer',
            'company': 'Engineering Solutions'
        }
        self.invalid_payload = {
            'name': '',
            'age': 36,
            'position': 'sr. engineer',
            'company': 'Engineering Solutions'
        }

    def test_valid_update(self):
        response = client.put(
            reverse('get_delete_update_api', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update(self):
        response = client.put(
            reverse('get_delete_update_api', kwargs={'pk': self.john.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class DeleteSingleTest(TestCase):
    ''' Test module for deleting an existing record '''

    def setUp(self):
        self.john = API.objects.create(
            name='John Smith', age=36, position='engineer', company='Engineering Consultants')
        self.jordan = API.objects.create(
            name='Jordan Stevens', age=42, position='program manager', company='San Diego Group')

    def test_valid_delete(self):
        response = client.delete(
            reverse('get_delete_update_api', kwargs={'pk': self.john.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete(self):
        response = client.delete(
            reverse('get_delete_update_api', kwargs={'pk': 16}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)    

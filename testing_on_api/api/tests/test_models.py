from django.test import TestCase
from ..models import API

class APITest(TestCase):
    ''' Test module for API model '''

    def setUp(self):
        API.objects.create(
            name='John Smith', age=36, position='engineer', company='Engineering Consultants')
        API.objects.create(
            name='Jordan Stevens', age=42, position='program manager', company='San Diego Group')

    def test_get_position(self):
        api_john = API.objects.get(name='John Smith')
        api_jordan = API.objects.get(name='Jordan Stevens')
        self.assertEqual(
            api_john.get_position(), 'John Smith works as engineer.')
        self.assertEqual(
            api_jordan.get_position(), 'Jordan Stevens works as program manager.')

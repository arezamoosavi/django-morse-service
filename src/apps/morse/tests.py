from django.test import TestCase
from django.urls import reverse
from rest_framework import status

# Create your tests here.
class Test_API(TestCase):

    def test_translation_and_queue(self):

        url = reverse('morse-api:translate')
        data = {'sentence':"Hello from Iran"}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['morse_code'], "......-...-..---/..-..-.-----/...-..--.")
        
        url = reverse('morse-api:queue')
        data = {"messege":response.data['morse_code']}
        
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['Task'], "Done")
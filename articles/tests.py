from urllib import response
from django.test import TestCase
from django.urls import reverse

# Create your tests here.
class HomePageTest(TestCase):
    def test1(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        
    def test2(self):
        response = self.client.get(reverse("Home"))
        self.assertTemplateUsed(response, "home.html") 
        
    def test3(self):
        response = self.client.get(reverse("Home"))
        self.assertEqual(response.status_code, 200)

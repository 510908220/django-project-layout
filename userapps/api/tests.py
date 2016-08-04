
from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from userapps.api.models import Shop


class AnimalTestCase(TestCase):

    def setUp(self):
        Shop.objects.all().delete()
        Shop.objects.create(name="apple")
        Shop.objects.create(name="xiaomi")

    def test_animals_can_speak(self):
        """Animals that can speak are correctly identified"""
        apple = Shop.objects.get(name="apple")
        xiaomi = Shop.objects.get(name="xiaomi")
        self.assertEqual(apple.name, 'apple')
        self.assertEqual(apple.name, 'xiaomi')

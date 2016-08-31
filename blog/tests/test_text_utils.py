from django.test import TestCase
from blog.utils.textUtils import add


class AnimalTestCase(TestCase):

    def test_add(self):
        self.assertEqual(add(1, 2), 3)

    def test_2(self):
        self.assertEqual(5, 2 + 4)
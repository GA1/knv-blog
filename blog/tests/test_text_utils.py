from django.test import TestCase
from blog.utils.textUtils import extract_first_three_lines_or_200_Chars


class AnimalTestCase(TestCase):

    def test_add(self):
        self.assertEqual(extract_first_three_lines_or_200_Chars("b"), "asdf")

    def test_add3(self):
        self.assertEqual(4, 2 + 2)

    def test_2(self):
        self.assertEqual(5, 2 + 4)
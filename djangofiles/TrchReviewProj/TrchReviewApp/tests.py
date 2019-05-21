from django.test import TestCase
from .models import TechType, Product, Review

# Create your tests here.
class TechTypeTest(TestCase):
    def test_string(self):
        type=TechType(techtypename='laptop')
        self.assertEqual(str(TechType),type.techtypename)
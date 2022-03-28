from django.test import TestCase, Client
from django.urls import reverse
from .service import CalculateAge

# Create your tests here.
class CalculateAgeTest(TestCase):
    def test_display_age(self):
        dob = '2021-06-11'
        cal_age = CalculateAge()
        age = cal_age.display_age(dob)
        self.assertEqual(age, '1  Years   3  Months  and 14  Days')

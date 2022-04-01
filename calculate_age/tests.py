from django.test import TestCase, Client
from django.urls import reverse
from .service import CalculateAge
import time
from datetime import date, datetime

# Create your tests here.
class CalculateAgeTest(TestCase):
    def test_display_age(self):
        dob = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d') # current date
        print(dob)
        cal_age = CalculateAge()
        age = cal_age.display_age(dob).get('result')
        self.assertEqual(age, '0  Years   0  Months  and 0  Days')
    
    def test_display_age_error(self):
        dob = ''
        cal_age = CalculateAge()
        age = cal_age.display_age(dob).get('error')
        self.assertEqual(age, 'Please enter a valid date')

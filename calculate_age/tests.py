from django.test import TestCase, Client
from django.urls import reverse
from .service import Calculate
import time
from datetime import date, datetime

# Create your tests here.
class CalculateAgeTest(TestCase):
    def test_display_age(self):
        dob = datetime.utcfromtimestamp(time.time()).strftime('%Y-%m-%d') # current date
        cal_age = Calculate()
        age = cal_age.display_age(dob).get('result')
        self.assertEqual(age, '0  Years   0  Months  and 0  Days')
    
    def test_display_age_error(self):
        dob = ''
        cal_age = Calculate()
        age = cal_age.display_age(dob).get('error')
        self.assertEqual(age, 'Please enter a valid date')

    def test_date_from_days_empty_error(self):
        days = ''
        cal_age = Calculate()
        result = cal_age.display_date_from_days(days).get('error')
        self.assertEqual(result, 'Days can not be empty')

    def test_date_from_days_negative_error(self):
        days = -1
        cal_age = Calculate()
        result = cal_age.display_date_from_days(days).get('error')
        self.assertEqual(result, 'Days can not be negative')

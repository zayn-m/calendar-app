from urllib import request
from django.shortcuts import render
from datetime import date, datetime
import numpy as np
from django.views.generic import TemplateView
from .service import CalculateAge
import time

# Create your views here.
class CalculateAgeView(TemplateView):
    template_name = "index.html"

    def post(self, request, **kwargs):
        date_of_birth = request.POST['date']
        cal_age = CalculateAge()
        response = cal_age.display_age(date_of_birth)
        context = {
            "date_of_birth": date_of_birth,
            "age": response.get('result') or None,
            "error": response.get('error') or None
        }
        return super(TemplateView, self).render_to_response(context)

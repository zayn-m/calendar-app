from django.contrib import admin
from django.urls import path

from calculate_age.views import CalculateAgeView, DateFromDays

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CalculateAgeView.as_view()),
    path('date/', DateFromDays.as_view()),
]

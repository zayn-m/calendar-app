from django.contrib import admin
from django.urls import path

from calculate_age.views import CalculateAgeView, DateFromDays, Events

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CalculateAgeView.as_view()),
    path('date/', DateFromDays.as_view()),
    path('events/', Events.as_view()),
]

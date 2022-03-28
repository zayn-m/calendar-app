from django.contrib import admin
from django.urls import path

from calculate_age.views import CalculateAgeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', CalculateAgeView.as_view()),
]

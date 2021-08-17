from django.urls import path

from main.views import ListStatistics

app_name = "main"

urlpatterns = [
    path('statistics/', ListStatistics.as_view()),
]
